# ViewForge

**ViewForge** is a modern Python desktop UI framework that renders HTML and web components inside a [pywebview](https://github.com/r0x0r/pywebview) window.

It supports component-based rendering, declarative event registration, and a clean event bridge using a single JavaScript function and dynamic Python handler resolution.

---

## ✨ Features

* ✅ Component-based architecture (Text, Button, Box, Stack, etc.)
* 🔗 Declarative event binding via `@handler()`
* 🔁 Single JS function dispatcher: `vf('event_name', ...args)`
* 🔐 Central Python event router: `handle_event(name, *args)`
* ⚡ Hot reload with Ctrl+R
* 🧩 Flexible styling via CSS-style dicts
* 🧠 Easy to extend with routing, signals, forms

---

## 🔧 Project Structure

```
viewforge/
├── app.py            # App lifecycle + pywebview integration
├── render.py         # HTML template and vf() injection
├── registry.py       # @handler() decorator + handler storage
├── component.py      # Base class for UI components
├── ui/               # Button, Text, Box, Stack, etc.
└── main.py           # Your app's entry point
```

---

## 🚀 Usage

### 1. Define a handler

```python
from viewforge.registry import handler

@handler()
def handle_click():
    print("Button clicked!")
```

### 2. Use the handler in a Button

```python
Button("Click Me", on_click=handle_click)
```

### 3. Launch your app

```python
from viewforge.app import App
App().run(build)
```

---

## 🧠 How Events Work

* You define handlers with `@handler()` → gives each one a name like `on_handle_click`
* Buttons generate HTML like:

  ```html
  <button onclick="vf('on_handle_click')">Click</button>
  ```
* The global JS `vf(...)` function calls Python via `pywebview.api.handle_event(...)`
* The `API` class routes it:

  ```python
  def handle_event(self, name, *args):
      return handler_registry.get()[name](*args)
  ```

---

## 🧪 Debug Tips

* Click too early? `vf(...)` retries until `handle_event` is ready
* Need to run JS *after* bridge is ready?

  ```js
  window.viewforge.ready(() => {
    vf("on_startup")
  })
  ```

---

## 📦 Coming Soon

* ✅ Form components with `on_submit`
* 🔁 Two-way binding via signals
* 🌐 Client-side routing
* 🎨 Theming and layout engine

---

## 🧼 Philosophy

**ViewForge** keeps your Python UI declarative, debuggable, and close to the metal — no build tools, no TypeScript, just dynamic HTML rendered with native Python logic.

> Build UIs in Python. Render like the web.
