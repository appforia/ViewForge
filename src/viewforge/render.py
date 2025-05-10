HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <script>
window.addEventListener("keydown", (e) => {{
  if (e.ctrlKey && e.key === "r") {{
    location.reload();
  }}
}});

function vf(name, ...args) {{
  if (window.pywebview?.api?.handle_event) {{
    window.pywebview.api.handle_event(name, ...args);
  }} else {{
    console.warn("[vf] Handler not ready for:", name);
    setTimeout(() => vf(name, ...args), 100);
  }}
}}

window.viewforge = {{
  readyQueue: [],
  ready(fn) {{
    if (window.pywebview?.api?.handle_event) {{
      fn();
    }} else {{
      this.readyQueue.push(fn);
      const check = () => {{
        if (window.pywebview?.api?.handle_event) {{
          while (this.readyQueue.length > 0) {{
            this.readyQueue.shift()();
          }}
        }} else {{
          setTimeout(check, 50);
        }}
      }};
      check();
    }}
  }}
}};
  </script>
</head>
<body>
  <div style="padding: 2rem; font-family: sans-serif;">
    {content}
  </div>
</body>
</html>"""


def render_html(components, title="ViewForge"):
    rendered = "\n".join(c.render() for c in components)
    return HTML_TEMPLATE.format(title=title, content=rendered)
