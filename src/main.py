from viewforge.app import App
from viewforge.components import (
    StackFrame, Text, TextInput, Button,
    GridFrame, AbsoluteFrame, Positioned
)

app = App()

@app.handler
def confirm(name, email):
    return {
        "message": {"name": name, "email": email},
        "clear_form": True
    }

app.configure(
    title="Grid & Absolute Layouts",
    size=(600, 500),
    padding=20
).add(
    StackFrame().configure(padding=12, gap=24).add(
        Text("Grid Layout Demo"),
        GridFrame(columns=2, gap=10).add(
            Text("Name:"), TextInput(name="name", placeholder="Full Name"),
            Text("Email:"), TextInput(name="email", placeholder="Email Address")
        ),
        Button("Submit", handler=confirm, bind=["name", "email"]),
        Text("Absolute Layout Demo"),
        AbsoluteFrame(width=500, height=150).add(
            Positioned(Text("Floating label"), x=20, y=20),
            Positioned(Button("Click Me", handler=lambda: "Absolute clicked!"), x=300, y=100)
        )
    )
).start()
