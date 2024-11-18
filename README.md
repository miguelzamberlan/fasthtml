# Projetos de Demonstração do FastHTML

Este repositório contém arquivs de demonstração que mostram o uso da biblioteca FastHTML com diferentes frameworks CSS: **Bootstrap**, **Pico CSS** e **Tailwind CSS**. Cada projeto ilustra como o FastHTML pode ser utilizado para criar aplicações web dinâmicas com código simples e limpo.

## Arquivos do Projeto

1. **`mainbootstrap.py`**
   - **Descrição**: Uma aplicação de gerenciamento de tarefas estilizada com Bootstrap. Funcionalidades incluem:
     - Gerenciamento dinâmico de lista de tarefas.
     - Modais para confirmações.
     - Uso de componentes do Bootstrap para estilização e responsividade.
   - **Framework CSS**: [Bootstrap 5](https://getbootstrap.com/).

2. **`mainpico.py`**
   - **Descrição**: Uma aplicação simplificada de gerenciamento de tarefas estilizada com Pico CSS. Funcionalidades incluem:
     - Design leve e responsivo.
     - Interface limpa para formulários e lista de tarefas.
   - **Framework CSS**: [Pico CSS](https://picocss.com/).

3. **`mainshared.py`**
   - **Descrição**: Uma aplicação de gerenciamento de tarefas estilizada com Tailwind CSS e componentes do `shad4fast`. Funcionalidades incluem:
     - Elementos avançados de interface como diálogos e cards.
     - Lista de tarefas dinâmica e formulários de entrada.
   - **Framework CSS**: [Tailwind CSS](https://tailwindcss.com/).

## Executando as Aplicações

Cada aplicação é um app FastAPI e pode ser iniciada usando o `uvicorn`. Por exemplo, para rodar o arquivo `mainshared.py`, use:

```bash
uvicorn mainshared:app --reload
```

### Etapas:

1. Clone este repositório.
2. Certifique-se de que o Python 3.7+ está instalado.
3. Instale as dependências necessárias para `FastHTML` e `Shad4FastHtml `:
   ```bash
   pip install fastapi uvicorn fasthtml shad4fast
   ```
4. Execute a aplicação desejada com:
   ```bash
   uvicorn <nome_do_arquivo>:app --reload
   ```
   Substitua `<nome_do_arquivo>` por `mainbootstrap`, `mainpico` ou `mainshared`, conforme necessário.

## Dependências

- **FastHTML**: Para renderização de HTML.
- **FastLite**: Para operações com banco de dados.

## Contribuições

Sinta-se à vontade para fazer um fork deste repositório e experimentar os projetos. Contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT.
