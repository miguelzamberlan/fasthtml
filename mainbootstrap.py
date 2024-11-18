from dataclasses import dataclass
from fasthtml.common import (
    fast_app,
    Div,
    serve,
    Card,
    Script,
    Link,
    Input,
    Button,
    Html,
    H1,
    H5,
    Head,
    Title,
    Form,
    Li,
    Ul,
)
from fastlite import database


app, routes = fast_app(
    # "dados.db",
    live=True,
    debug=True,
    pico=False,
)

db = database("dados.db")


@dataclass
class Tarefa:
    id: int
    tarefa: str


lista_tarefas = db.create(Tarefa, pk="id")


headers = [
    Script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css",
    ),
    # Link(rel="icon", href="pirate.png", type="image/png"),
    Script(src="https://unpkg.com/htmx.org@2.0.3"),
    Title("Lista de Tarefas"),
]


def modal(mensagem, tipo, nome):
    return Div(
        Div(
            Div(
                Div(
                    H5("Confirmação", cls="modal-title"),
                    Button(
                        cls="btn-close",
                        data_bs_dismiss="modal",
                        aria_label="Close",
                    ),
                    cls="modal-header",
                ),
                Div(
                    Div(
                        mensagem,
                        cls="modal-body",
                    ),
                    cls="modal-body",
                ),
                Div(
                    Button(
                        "Cancelar",
                        cls="btn btn-secondary",
                        data_bs_dismiss="modal",
                    ),
                    Button(
                        "Excluir",
                        hx_delete=f"/deletar/{nome}",
                        hx_swap="outerHTML",
                        target_id=f"tarefa-{nome}",
                        data_bs_dismiss="modal",
                        cls="btn btn-danger",
                    ),
                    cls="modal-footer",
                ),
                cls="modal-content",
            ),
            cls="modal-dialog",
        ),
        cls="modal fade",
        id=f"modal{nome}",
        tabindex="-1",
    )


def field_tarefa():
    return Input(
        type="text",
        id="tarefa",
        placeholder="Insira a tarefa",
        required=True,
        hx_swap_oob="true",
        cls="form-control",
    )


def gerar_formulario():
    formulario = Form(
        Div(
            field_tarefa(),
            Button(
                "Inserir",
                hx_post="/adicionar",
                target_id="lista-tarefas",
                hx_swap="beforeend",
                cls="btn btn-primary",
            ),
            cls="input-group p-2",
        ),
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


def renderizar_tarefa(tarefa):

    return Li(
        tarefa.tarefa,
        Button(
            "Excluir",
            hx_target=f"#modal{tarefa.id}",
            hx_trigger="click",
            data_bs_toggle="modal",
            data_bs_target=f"#modal{tarefa.id}",
            cls="btn btn-sm btn-danger",
        ),
        modal(f"Confirma a exclusão da tarefa {tarefa.tarefa}?", "danger", tarefa.id),
        id=f"tarefa-{tarefa.id}",
        cls="list-group-item d-flex justify-content-between align-items-start",
    )


@routes("/")
def home():
    formulario = gerar_formulario()
    lista_tarefas_render = gerar_lista_tarefas(lista_tarefas=lista_tarefas)
    return (
        Html(
            Head(*headers),
            H1("Lista de Tarefas", cls="text-2xl"),
            Div(
                formulario,
                cls="card justify-center mt-4 p-3",
            ),
            Card(lista_tarefas_render),
            cls="container mx-auto mt-4",
        ),
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
