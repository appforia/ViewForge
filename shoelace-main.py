from viewforge.core import App
from viewforge.core.registry import handler
from viewforge.state.signal import Signal
from viewforge.ui.elements import Text
from viewforge.ui.layout import Stack
from viewforge.plugins.shoelace.buttons import ShoelaceButton

# Reactive state
count = Signal(0)

# Handlers (must be registered)
@handler(name='increment')
def increment():
    count.set(count() + 1)
    print(count())

@handler(name='decrement')
def decrement():
    count.set(count() - 1)
    print(count())

# UI layout
def build():
    return Stack([
        Text("🔢 Shoelace Counter", css={"font_size": "1.5rem", "margin_bottom": "1rem"}),
        Text(count),
        Stack([
            ShoelaceButton("➕ Increment", on_click=increment),
            ShoelaceButton("➖ Decrement", on_click=decrement)
        ], css={"gap": "1rem"})
    ], css={"padding": "2rem", "gap": "1rem"})

# Run app
if __name__ == "__main__":
    App().run(build, True)
