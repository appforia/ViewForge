from pathlib import Path

ASSET_DIR = Path(__file__).parent / "assets"

def read_asset(name: str) -> str:
    return (ASSET_DIR / name).read_text(encoding="utf-8")

HTML_TEMPLATE = read_asset("template.html")
STYLE = read_asset("style.css")
SCRIPT = read_asset("shoelace-bundle.js")

def render_html(components, title="ViewForge App"):
    rendered = "\n".join(c.render() for c in components)

    html = (
        HTML_TEMPLATE
        .replace("{{title}}", title)
        .replace("{{style}}", STYLE)
        .replace("{{script}}", SCRIPT)
        .replace("{{content}}", rendered)
    )
    return html
