from viewforge.app import App
from viewforge.ui import Text, Stack

def build():
    return [
        Stack([
            Text("Hello from main.py!"),
            Text("Wow! Yes i know")
        ])
    ]

if __name__ == "__main__":
    App().run(build())
