from viewforge.app import App
from viewforge.signal import Signal
from viewforge.registry import handler
from viewforge.ui.text import Text
from viewforge.ui.stack import Stack
from viewforge.ui.input import TextInput


# Create a signal to hold the user's name
name = Signal("")

@handler()
def name_changed(value: str):
    print("Input changed:", value)
    name.set(value)


def build():
    return [
        Stack([
            Text("What's your name?", tag="h2"),
            TextInput(name="firstName", bind=name, on_input=name_changed),
            Text(name, size="md", color="gray")
        ], css={"gap": "1rem", "padding": "2rem"})
    ]


if __name__ == "__main__":
    App().run(build)
