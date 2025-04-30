# src/viewforge/theme/loader.py
import threading
from viewforge.state import state

class ThemeManager:
    def __init__(self):
        self.window = None
        self.current_theme = "light"
        self.frontend_ready = False

    def attach_webview(self, webview_window):
        self.window = webview_window
        print("[ThemeManager] WebView attached")

        # If frontend already ready, inject now
        if self.frontend_ready:
            self._inject_theme()

    def mark_js_ready(self):
        print(f"[ThemeManager] JS signaled readiness → injecting theme: {self.current_theme}")
        self.frontend_ready = True

        def try_later():
            if self.window:
                print("[ThemeManager] Retrying theme injection...")
                self._inject_theme()
            else:
                print("[ThemeManager] Still waiting on WebView... retrying in 100ms")
                threading.Timer(0.1, try_later).start()

        try_later()

    def set_theme(self, theme: str):
        self.current_theme = theme
        state.set("theme", theme)

        if self.window and self.frontend_ready:
            self._inject_theme()
        else:
            print("[ThemeManager] Theme change received, but not ready. Deferring.")

    def _inject_theme(self):
        if not self.window:
            print("[ThemeManager] Cannot inject theme: window not attached")
            return

        print(f"[ThemeManager] Injecting theme: {self.current_theme}")
        css_path = f"./css/themes/{self.current_theme}.css"
        js = f"""
        (function() {{
            const existing = document.getElementById('theme-css');
            if (existing && existing.href.includes('{self.current_theme}.css')) return;
            if (existing) existing.remove();
            const link = document.createElement('link');
            link.id = 'theme-css';
            link.rel = 'stylesheet';
            link.href = '{css_path}';
            document.head.appendChild(link);
        }})();
        """
        self.window.evaluate_js(js)

# Singleton
theme_manager = ThemeManager()
