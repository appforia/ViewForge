# ViewForge

**ViewForge** is a minimal, component-based UI framework for building desktop apps using Python and modern Web Components. It leverages [pywebview](https://pywebview.flowrl.com/) to render HTML/CSS UI and supports hot-reload for rapid development.

---

## ✨ Features

- 🧱 Component primitives (Text, Stack, Form, SelectBox, etc.)
- 🔁 Signal-based state management
- 🔀 Built-in router with route params and query strings
- ⚡ Hot-reload CLI: `viewforge-reload`
- 💡 Works with `main.py` by default
- 🧩 Extendable with custom JS components via bridge

---

## 📦 Installation

```bash
pip install -e .
```

> Make sure you have `pywebview` and `watchdog` installed in your environment.

---

## 🚀 Quick Start

Create a `main.py` in your project root:

```python
from viewforge.ui import Text, Stack

def build():
    return [
        Stack([
            Text("✅ Hello from ViewForge"),
            Text("✏️ Edit and save this file to trigger live reload")
        ])
    ]
```

Start the dev server:

```bash
viewforge-reload
```

✔️ It will automatically reload when you edit any `.py` file in the project.

---

## 🔥 Hot Reload CLI

ViewForge ships with a built-in CLI tool:

```bash
viewforge-reload [optional_module.py]
```

- If no argument is given, it loads `main.py` from the current directory.
- Watches all `.py` files in the project folder
- Reloads the UI on save
- Handles exceptions and shows them in the app

---

## 🧪 Sample Project Structure

```
project/
├── main.py                  # App entry point
├── viewforge/               # Installed library (editable)
└── pyproject.toml           # CLI entry point defined here
```

---

## 🔧 Defining Your UI

You create a tree of components using primitives like:

```python
from viewforge.ui import Text, Stack, TextInput, Button

def build():
    return [
        Stack([
            Text("Login"),
            TextInput(name="username"),
            Button("Submit")
        ])
    ]
```

---

## 🔌 Bridge Support

You can register Python functions as JS handlers via the bridge:

```python
from viewforge.bridge import register_handler

def say_hello(name):
    print(f"Hello, {name}!")

register_handler("greet", say_hello)
```

---

## 🧭 Routing

```python
from viewforge.router import create_router

router = create_router()
router.add_route("/users/<id>", user_view)

app.run([RouterView(router)])
```

Use `RouteLinkButton("Go", "/users/5")` to navigate.

---

## 🧰 Development Tips

- Use `Signal()` to bind state to inputs
- Reload happens automatically on `.py` file changes
- Keep `main.py` as your entry point for smooth CLI support
- Avoid calling `webview.start()` yourself — use `App.run()` only

---

## 📜 License

MIT © 2025 Israel Dryer
