
# FastHTML Demonstration Projects

This repository contains demonstration projects showcasing the use of the FastHTML library with different CSS frameworks: **Bootstrap**, **Pico CSS**, and **Tailwind CSS**. Each project illustrates how FastHTML can be used to create dynamic web applications with simple and clean code.

## Project Files

1. **`mainbootstrap.py`**
   - **Description**: A task management application styled using Bootstrap. Features include:
     - Dynamic task list management.
     - Modals for confirmation.
     - Use of Bootstrap components for styling and responsiveness.
   - **CSS Framework**: [Bootstrap 5](https://getbootstrap.com/).

2. **`mainpico.py`**
   - **Description**: A simplified task management app styled with Pico CSS. Features include:
     - Lightweight design and responsiveness.
     - Clean forms and task list interface.
   - **CSS Framework**: [Pico CSS](https://picocss.com/).

3. **`mainshared.py`**
   - **Description**: A task management app styled with Tailwind CSS and `shad4fast` components. Features include:
     - Advanced UI elements like dialogs and cards.
     - Dynamic task list and input forms.
   - **CSS Framework**: [Tailwind CSS](https://tailwindcss.com/).

## Running the Applications

Each application is a FastAPI app and can be started using `uvicorn`. For example, to run the `mainshared.py` file, use:

```bash
uvicorn mainshared:app --reload
```

### Steps:

1. Clone this repository.
2. Ensure Python 3.7+ is installed.
3. Install the necessary dependencies for `FastHTML` and `FastAPI`:
   ```bash
   pip install fastapi uvicorn fasthtml fastlite shad4fast
   ```
4. Run the desired application with:
   ```bash
   uvicorn <filename>:app --reload
   ```
   Replace `<filename>` with `mainbootstrap`, `mainpico`, or `mainshared` as needed.

## Dependencies

- **FastHTML**: For HTML rendering.
- **FastAPI**: For creating the web server.
- **FastLite**: For database operations.

## Contributions

Feel free to fork this repository and experiment with the projects. Contributions are welcome!

## License

This project is licensed under the MIT License.
