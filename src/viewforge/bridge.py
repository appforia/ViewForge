# src/viewforge/bridge.py

from viewforge.theme.loader import theme_manager
from viewforge.state import state

class JSBridge:
    def __init__(self):
        self.handlers = {
            "theme": self.get_theme,
            "frontend:ready": self.mark_ready
        }

    def receiveMessage(self, message: str):
        print("[JSBridge] Received:", message)

        if ":" in message:
            cmd, arg = message.split(":", 1)
            if cmd == "theme":
                return self.set_theme(arg.strip())

        handler = self.handlers.get(message)
        return handler() if handler else f"Echo: {message}"

    def mark_ready(self):
        print("[JSBridge] Received frontend:ready")
        theme_manager.mark_js_ready()
        return "ack"

    def get_theme(self):
        return state.get("theme", "light")

    def set_theme(self, theme):
        theme_manager.set_theme(theme)
        return f"Theme set to {theme}"