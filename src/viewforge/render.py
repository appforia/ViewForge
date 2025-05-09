from viewforge.bridge import generate_js_stubs

TEMPLATE_HEAD = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>ViewForge</title>
  <script>
{js_stubs}

window.addEventListener('keydown', (e) => {{
  if (e.ctrlKey && e.key === 'r') {{
    console.log('Hot reload triggered');
    if (window.pywebview) {{
      window.pywebview.api.reload();
    }} else {{
      location.reload();
    }}
  }}
}});
  </script>
</head>
<body>
"""

TEMPLATE_BODY = """<div style='padding: 2rem; font-family: sans-serif;'>
  {content}
</div>
</body>
</html>
"""


def render_html(components):
    rendered = "\n".join(c.render() for c in components)
    js_stubs = generate_js_stubs()
    return TEMPLATE_HEAD.format(js_stubs=js_stubs) + TEMPLATE_BODY.format(content=rendered)
