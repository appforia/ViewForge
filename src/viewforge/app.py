import uuid
from functools import wraps
from typing import Optional, Callable
import webview
from viewforge.bridge import JSBridge

_current_app = None

class App:
    def __init__(self):
        global _current_app
        _current_app = self
        self.config = {}
        self.children = []
        self.handlers = {}
        self.bridge = JSBridge()

    @staticmethod
    def current():
        if _current_app is None:
            raise RuntimeError("App.current() called before App() was initialized.")
        return _current_app

    def configure(self, **kwargs):
        self.config.update(kwargs)
        return self

    def add(self, *components):
        self.children.extend(components)
        return self

    def handler(self, func: Optional[Callable] = None, *, name: Optional[str] = None, namespace: Optional[str] = None):
        def decorator(f):
            base_name = name or f.__name__
            handler_name = f"{namespace}:{base_name}" if namespace else base_name
            f._handler_name = handler_name

            @wraps(f)
            def wrapped(*args, **kwargs):
                print(f"[App] Calling handler: {handler_name}({', '.join(map(repr, args))})")
                return f(*args, **kwargs)

            self.handlers[handler_name] = wrapped
            self.bridge.register_handler(handler_name, wrapped)
            return wrapped

        return decorator(func) if func else decorator

    def register_anonymous(self, func):
        anon_name = f"anon_{uuid.uuid4().hex[:8]}"
        func._handler_name = anon_name
        self.handlers[anon_name] = func
        self.bridge.register_handler(anon_name, func)
        return anon_name

    def _generate_html(self):
        body = ''.join(child.render() for child in self.children)
        return f"""<!DOCTYPE html>
<html>
<head><title>{self.config.get('title', 'App')}</title></head>
<body style="margin:0;padding:{self.config.get('padding', 0)}px;">
{body}
<script>
function sendBoundForm(btn) {{
  const handler = btn.dataset.handler;
  const bindList = JSON.parse(btn.dataset.bind || "[]");
  const args = bindList.map(id => {{
    const el = document.getElementById(id);
    if (!el) return null;
    return el.type === "checkbox" ? el.checked : el.value;
  }});

  const payload = JSON.stringify({{ handler, args }});
  window.pywebview.api.receiveMessage(payload).then(result => {{
    const errorBox = document.getElementById("validation-message");

    if (typeof result === "object" && result.error) {{
      if (errorBox) {{
        errorBox.textContent = result.message || "Validation failed";
        errorBox.style.display = "block";
      }}
    }} else {{
      if (errorBox) errorBox.style.display = "none";
      alert(typeof result === "object" ? result.message : result);

      if (typeof result === "object" && result.clear_form) {{
        bindList.forEach(id => {{
          const el = document.getElementById(id);
          if (el) {{
            if (el.type === "checkbox") el.checked = false;
            else el.value = "";
          }}
        }});
      }}
    }}
  }});
}}
</script>
</body>
</html>"""

    def start(self):
        html = self._generate_html()
        with open("ui.html", "w", encoding="utf-8") as f:
            f.write(html)
        webview.create_window(
            self.config.get("title", "App"),
            "ui.html",
            width=self.config.get("size", (400, 400))[0],
            height=self.config.get("size", (400, 400))[1],
            js_api=self.bridge
        )
        webview.start()
