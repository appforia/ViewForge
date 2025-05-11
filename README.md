# ViewForge

**ViewForge** is a modern Python desktop UI framework that renders HTML and web components inside a [pywebview](https://github.com/r0x0r/pywebview) window.

It supports component-based rendering, declarative event registration, reactive state with signals, and flexible routing — all in Python.

---

## ✨ Features

* ✅ Component-based architecture (Text, Button, Stack, etc.)
* 🔗 Declarative event binding via `@handler()`
* 🧠 Central Python event router for dynamic dispatch
* 🧩 Flexible styling via CSS-style dicts
* 🌐 Built-in router with support for path params and query strings
* ⚡ Hot reload with `Ctrl+R`
* 🔁 Signals for reactive state
* 📦 Modular, extensible, no build step required

---

## 📁 Project Structure

```
viewforge/
├── core/             # App, Component, Registry
├── ui/               # elements/, layout/, links/
├── routing/          # route decorators, RouterView
├── state/            # Signal, Store
├── rendering/        # DOM and HTML rendering logic
├── utils/            # CSS, JS utilities, case handling
├── adapters/         # Optional UI system adapters (Shoelace, BeerCSS)
├── plugins/          # Debug tools, hot reload
└── main.py           # App entry point
```

---

## 🚀 Getting Started

### 1. Define a handler

```python
from viewforge.core.registry import handler

@handler()
def handle_click():
    print("Button clicked!")
```

### 2. Use the handler in a Button

```python
from viewforge.ui.elements import Button

Button("Click Me", on_click=handle_click)
```

### 3. Launch the app

```python
from viewforge.core import App

App().run(lambda: [Button("Hi")])
```

---

## 🧠 How Events Work

* You define Python handlers with `@handler()` → they get a unique name like `on_handle_click`
* Components like `Button` render HTML like:

  ```html
  <sl-button onclick="vf('on_handle_click')">Click</sl-button>
  ```

* The global `vf(...)` JS function relays to Python via `pywebview.api.handle_event(...)`
* The Python router calls your function:

  ```python
  def handle_event(self, name, *args):
      return handler_registry.get()[name](*args)
  ```

---

## 🌐 Routing Example

```python
from viewforge.routing import route

@route("/user/<id>", "User Profile")
def user_profile(params, route):
    return Text(f"Viewing user {params['id']}")
```

---

## 💡 Signals

```python
from viewforge.state import Signal

count = Signal(0)

Button("Increment", on_click=lambda: count.set(count.get() + 1))
Text(lambda: f"Count: {count.get()}")
```

---

## 🔧 Advanced Tips

* All components support `style={}` for CSS properties
* You can nest layout containers like `Stack`, `Box`, or build your own
* Router supports dynamic segments and query strings

---

## 📦 Coming Soon

* ✅ FormGroup with validation
* 🧭 View decorators for route views
* 🌈 Light/dark theme switching

---

## 🧼 Philosophy

**ViewForge** is minimal by design — no JavaScript build steps, no virtual DOM diffing — just clean Python and direct HTML rendering.

> Build UIs in Python. Render like the web.
