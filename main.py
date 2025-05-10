from viewforge.app import App
from viewforge.ui.text import Text
from viewforge.ui.box import Box
from viewforge.ui.stack import Stack
from viewforge.ui.button import Button
from viewforge.registry import handler


@handler()
def handle_click():
    print("Button was clicked!")


def build():
    return [
        Stack([
            Text(
                "Welcome to ViewForge",
                tag="h1",
                size="4xl",
                weight="bold",
                align="center",
                color="white",
                background="royalblue",
                padding_y=16
            ),
            Text(
                "This is a simple demo using Box, Stack, Text, and Button.",
                size="md",
                align="center",
                color="gray"
            ),
            Box([
                Text("This is inside a box."),
                Button("Click Me", on_click=handle_click, padding=12, rounded="md", background="green", color="white")
            ],
                padding=24,
                shadow="lg",
                rounded="lg",
                background="lightgray"
            )
        ],
            css={"padding": "2rem", "gap": "2rem"})
    ]


if __name__ == "__main__":
    components = build()
    App().run(components)
