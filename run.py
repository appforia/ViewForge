import webview
import os

from viewforge.bridge import JSBridge
from viewforge.theme.loader import theme_manager

html_path = os.path.abspath("static/index.html")
bridge = JSBridge()

# Create the window
window = webview.create_window(
    "ViewForge",
    url=f"file://{html_path}",
    width=1280,
    height=800,
    js_api=bridge
)

def on_loaded():
    theme_manager.attach_webview(window)  # <-- THIS must be called


webview.start(func=on_loaded, debug=True)
