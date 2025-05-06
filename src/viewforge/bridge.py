import json

class JSBridge:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, name, func):
        self.handlers[name] = func

    def receiveMessage(self, payload: str):
        print("[Bridge] Raw payload:", payload)

        try:
            data = json.loads(payload)
            handler = data.get("handler")
            args = data.get("args", [])
        except Exception as e:
            print("[Bridge] Failed to parse payload:", e)
            return {"error": True, "message": "Invalid request format"}

        print(f"[Bridge] Call received: {handler}({args})")

        if handler in self.handlers:
            try:
                result = self.handlers[handler](*args)
                # Ensure the result is JSON-serializable
                return result if result is not None else ""
            except Exception as e:
                print("[Bridge] Handler error:", e)
                return {"error": True, "message": str(e)}
        else:
            return {"error": True, "message": f"No handler named '{handler}'"}
