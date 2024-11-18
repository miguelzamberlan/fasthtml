from dataclasses import dataclass
from fasthtml.common import fast_app, Div, serve, H1, Form
from fastlite import database

from shad4fast import (
    ShadHead,
    Button,
    Card,
    Input,
    Table,
    TableBody,
    TableCell,
    TableRow,
    TableHeader,
    TableHead,
    DialogTrigger,
    Dialog,
    DialogClose,
    Alert,
    DialogContent,
    DialogHeader,
    DialogTitle,
    DialogDescription,
    DialogFooter,
)

app, routes = fast_app(
    # "dados.db",
    live=True,
    debug=True,
    pico=False,
    hdrs=(ShadHead(tw_cdn=True, theme_handle=True),),
)

db = database("dados.db")


@dataclass
class Tarefa:
    id: int
    tarefa: str


lista_tarefas = db.create(Tarefa, pk="id")


def field_tarefa():
    return Input(type="text", id="tarefa", placeholder="Insira a tarefa", required=True, hx_swap_oob="true", cls="form-input")


def gerar_formulario():
    formulario = Form(
        Card(
            field_tarefa(),
            title="Adicionar Tarefa",
            description="Insira a tarefa e clique em Inserir.",
            footer=Div(
                Button(
                    "Inserir",
                    hx_post="/adicionar",
                    target_id="lista-tarefas",
                    hx_swap="beforeend",
                ),
            ),
        ),
        method="post",
        action="/adicionar",
    )

    return formulario


def gerar_lista_tarefas(lista_tarefas):
    itens_lista = [renderizar_tarefa(tarefa) for tarefa in lista_tarefas()]

    return itens_lista


def renderizar_tarefa(tarefa):
    return TableRow(
        TableCell(
            tarefa.tarefa,
        ),
        TableCell(
            Dialog(
                DialogTrigger("Excluir", variant="destructive"),
                DialogContent(
                    DialogHeader(
                        DialogTitle("Excluir Registro"),
                        DialogDescription("Tem certeza que deseja excluir este registro?"),
                    ),
                    DialogFooter(
                        DialogClose(
                            "Cancelar",
                        ),
                        DialogClose(
                            "Confirmar",
                            hx_delete=f"/deletar/{tarefa.id}",
                            hx_swap="outerHTML",
                            target_id=f"tarefa-{tarefa.id}",
                            variant="destructive",
                        ),
                    ),
                    cls="sm:max-w-[425px]",
                    state="closed",
                ),
                standard=True,
            ),
            cls="text-end",
        ),
        id=f"tarefa-{tarefa.id}",
    )


@routes("/")
def home():
    formulario = gerar_formulario()
    lista_tarefas_render = gerar_lista_tarefas(lista_tarefas=lista_tarefas)

    return Div(
        H1("Lista de Tarefas", cls="text-center text-2xl font-bold my-6"),
        Div(formulario),
        Alert(
            title="New message!",
            description="Open your messages to view more details.",
            cls="max-w-[100%] my-6",
            standard=False,
        ),
        Table(
            TableHeader(
                TableRow(
                    TableHead("Tarefa"),
                    TableHead("Ações", cls="text-end mr-4"),
                )
            ),
            TableBody(
                *lista_tarefas_render,
            ),
            id="lista-tarefas",
            cls="table-auto border border-collapse my-6",
        ),
        cls="container mx-auto p-4",
    )


@routes("/adicionar", methods=["post"])
def adicionar(tarefa: Tarefa):
    if tarefa:
        tarefa = lista_tarefas.insert(Tarefa(tarefa=tarefa.tarefa))

    return renderizar_tarefa(tarefa), field_tarefa()


@routes("/deletar/{posicao}", methods=["delete"])
def deletar(posicao: int):
    if posicao:
        lista_tarefas.delete(posicao)


serve()
