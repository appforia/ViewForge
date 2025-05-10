from viewforge.utils import apply_style_props, merge_styles


class Component:
    def __init__(self, default_style=None, css=None, **props):
        """
        default_style → the lowest precedence
        css → user override dict
        props → the highest precedence (shorthand props like padding=16)
        """
        final_style = apply_style_props(
            default_style or {},
            css or {},
            props
        )
        self.css_dict = final_style
        self.css = merge_styles(final_style)

    def style_attr(self) -> str:
        return f' style="{self.css}"' if self.css else ""

    def render(self) -> str:
        raise NotImplementedError()
