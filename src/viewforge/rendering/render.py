import os

def render_into_vite(components):
    rendered = "\n".join(c.render() for c in components)

    dist_path = os.path.abspath("dist/index.html")
    with open(dist_path, encoding="utf-8") as f:
        html = f.read()

    html = html.replace("<!--VIEWFORGE-CONTENT-->", rendered)

    out_path = os.path.abspath("web/index.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    return out_path