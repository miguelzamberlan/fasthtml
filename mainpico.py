from dataclasses import dataclass
from fasthtml.common import fast_app, Div, serve, Card, Button, Input, Titled, Form, A, H5, Li, Ul, Group, DialogX
from fastlite import database

app, routes = fast_app(
    live=True,
    debug=True,
)

db = database("dados.db")


@dataclass
class Tarefa:
    id: int
    tarefa: str


lista_tarefas = db.create(Tarefa, pk="id")


def field_tarefa():
    return Input(
        type="text",
        id="tarefa",
        placeholder="Insira a tarefa",
        required=True,
        hx_swap_oob="true",
    )


def gerar_formulario():
    formulario = Form(
        Group(
            field_tarefa(),
            Button(
                "Inserir",
                hx_post="/adicionar",
                target_id="lista-tarefas",
                hx_swap="beforeend",
            ),
        ),
        cls="mt-4",
    )

    return formulario


def gerar_lista_tarefas(lista_tarefas):
    itens_lista = [renderizar_tarefa(tarefa) for tarefa in lista_tarefas()]

    return Ul(
        *itens_lista,
        id="lista-tarefas",
        cls="mt-2 list-group",
        role="list",
    )


def toggle_dialog(event):
    dialog = event.find("#dlgtest")
    dialog.open = not dialog.open


def renderizar_tarefa(tarefa):

    hdr = Div(
        Button(
            aria_label="Close",
            rel="prev",
            onclick="document.getElementById('dlgtest').removeAttribute('open')",
        ),
        H5("Confirmação"),
    )
    ftr = Div(
        Button(
            "Cancelar",
            cls="secondary",
            onclick="document.getElementById('dlgtest').removeAttribute('open')",
        ),
        Button(
            "Confirmar",
            hx_delete=f"/deletar/{tarefa.id}",
            hx_swap="outerHTML",
            target_id=f"tarefa-{tarefa.id}",
            onclick="document.getElementById('dlgtest').removeAttribute('open')",
        ),
    )
    modal_delete = DialogX(f"Confirma a exclusão da tarefa {tarefa.tarefa}?", header=hdr, footer=ftr, open=False, id="dlgtest")

    return Li(
        tarefa.tarefa,
        " - ",
        A(
            "Excluir",
            onclick="document.getElementById('dlgtest').setAttribute('open', 'true')",
            cls="pico-background-pink-600",
        ),
        modal_delete,
        id=f"tarefa-{tarefa.id}",
        cls="list-group-item d-flex justify-content-between align-items-start",
    )


@routes("/")
def home():
    formulario = gerar_formulario()
    lista_tarefas_render = gerar_lista_tarefas(lista_tarefas=lista_tarefas)

    return Titled(
        "Lista de Tarefas",
        Div(
            formulario,
            cls="flex justify-center mt-4",
        ),
        Card(lista_tarefas_render),
    )


@routes("/adicionar", methods=["post"])
def adicionar(tarefa: Tarefa):
    print("Tarefa:", tarefa)
    if tarefa:
        tarefa = lista_tarefas.insert(Tarefa(tarefa=tarefa.tarefa))

    return renderizar_tarefa(tarefa), field_tarefa()


@routes("/deletar/{posicao}", methods=["delete"])
def deletar(posicao: int):
    if posicao:
        lista_tarefas.delete(posicao)


serve()
