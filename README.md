# ViewForge

**ViewForge** is a modular Python UI and workflow engine designed to simplify the development of reactive, desktop-style applications using modern Python techniques. It supports both dynamic and static UIs, plugin architecture, and clean separation of logic and layout.

> Licensed under the **GNU General Public License v3.0 or later (GPL-3.0-or-later)**.

---

## 🔧 Features

- 🔌 Plugin-friendly component architecture
- 🌗 Dynamic theme switching (light/dark/custom)
- 🎨 Declarative and fluent UI composition
- 🧠 Built-in state management and routing
- 🌐 WebView or native Tkinter-based rendering
- 💡 Inspired by frameworks like HeroUI and Zustand

---

## 📦 Installation

Install via pip (once published):

```bash
pip install viewforge
```

Or install from source:

```bash
git clone https://github.com/yourusername/viewforge.git
cd viewforge
pip install .
```

---

## 🚀 Getting Started

Here’s a minimal usage example:

```python
from viewforge import App, Window, Button

app = App()
window = Window(title="ViewForge Demo")

window.add(Button(text="Click Me"))
app.run(window)
```

---

## 🧪 Running Tests

Make sure you have `pytest` installed:

```bash
pip install pytest
```

Then run tests with:

```bash
pytest tests/
```

---

## 📄 License

This project is licensed under the terms of the **GNU General Public License v3.0 or later**.  
See the [full license text here](https://www.gnu.org/licenses/gpl-3.0.txt).

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome!  
Please [open an issue](https://github.com/yourusername/viewforge/issues) before submitting large changes.

---

## 📚 Resources

- 📦 PyPI: [pypi.org/project/viewforge](https://pypi.org/project/viewforge)
- 🗂 Source: [github.com/yourusername/viewforge](https://github.com/yourusername/viewforge)
- 📖 License: [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0.txt)
