from viewforge.app import App
from viewforge.signal import Signal
from viewforge.registry import handler
from viewforge.ui.checkbox import Checkbox
from viewforge.ui.text import Text
from viewforge.ui.stack import Stack
from viewforge.ui.textbox import TextBox
from viewforge.ui.selectbox import SelectBox

# Reactive signals
name = Signal("")
color = Signal("Red")
accept_terms = Signal(False)

@handler()
def toggle_accept(value: bool):
    accept_terms.set(value)

@handler()
def name_changed(value: str):
    name.set(value)


@handler()
def color_changed(value: str):
    color.set(value)


def build():
    return [
        Stack([
            Text("What's your name?", tag="h2"),
            TextBox(name="firstName", value=name(), on_input=name_changed),
            Text(name, size="md", color="gray"),

            Text("Choose a color:", tag="h2", css={"margin_top": "2rem"}),
            SelectBox(
                name="favoriteColor",
                options=["Red", "Green", "Blue"],
                selected=color,
                on_change=color_changed
            ),
            Text(color, size="md", color=color()),
            Checkbox(
                label="I agree to the terms",
                checked=accept_terms,
                on_change=toggle_accept
            )
        ], css={"gap": "1rem", "padding": "2rem"})
    ]


if __name__ == "__main__":
    App().run(build)
