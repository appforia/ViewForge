import re


def camel_to_kebab(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def snake_to_camel(name: str) -> str:
    parts = name.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])


def camel_to_snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def snake_to_kebab(name: str) -> str:
    return name.replace("_", "-")
