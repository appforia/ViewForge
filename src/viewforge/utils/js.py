import json


def js_func(name: str, *args):
    arg_str = ", ".join(json.dumps(arg) for arg in args)
    return f"{name}({arg_str})"
