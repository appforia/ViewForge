from typing import TypedDict, Literal, Any, Optional, Mapping, Unpack, Union

from viewforge.state.signal import Signal


class StylePropsDict(TypedDict, total=False):
    # 🧱 Layout & Positioning
    display: Literal["block", "inline", "flex", "grid", "none"]
    position: Literal["static", "relative", "absolute", "fixed", "sticky"]
    overflow: Literal["visible", "hidden", "scroll", "auto"]
    box_sizing: Literal["border-box", "content-box"]
    float: Literal["left", "right", "none"]
    clear: Literal["left", "right", "both", "none"]
    isolation: Literal["auto", "isolate"]
    top: Any
    right: Any
    bottom: Any
    left: Any
    inset: Any
    inset_block: Any
    inset_inline: Any
    z_index: int
    aspect_ratio: str
    visibility: Literal["visible", "hidden"]

    # 📦 Flex & Grid
    flex_direction: Literal["row", "row-reverse", "column", "column-reverse"]
    flex_wrap: Literal["nowrap", "wrap", "wrap-reverse"]
    flex_grow: int
    flex_shrink: int
    grid_template_columns: str
    grid_template_rows: str
    grid_row_start: str
    grid_row_end: str
    grid_column_start: str
    grid_column_end: str
    grid_auto_flow: Literal["row", "column"]
    grid_auto_columns: Any
    grid_auto_rows: Any
    gap: Any
    column_gap: Any
    row_gap: Any

    # 📏 Spacing & Sizing
    padding: Any
    padding_left: Any
    padding_right: Any
    padding_top: Any
    padding_bottom: Any
    padding_x: Any
    padding_y: Any
    margin: Any
    margin_left: Any
    margin_right: Any
    margin_top: Any
    margin_bottom: Any
    margin_x: Any
    margin_y: Any
    width: Any
    height: Any
    max_width: Any
    min_width: Any
    max_height: Any
    min_height: Any
    block_size: Any
    inline_size: Any

    # 🎨 Visual Styling
    background: str
    border: str
    border_radius: Any
    rounded: Literal["none", "sm", "md", "lg", "xl", "2xl", "full"]
    shadow: Literal["none", "sm", "md", "lg", "xl", "2xl", "inner"]
    box_shadow: str
    opacity: float
    color: str

    # ✍ Typography
    font_size: Any
    font_family: str
    font_style: Literal["normal", "italic", "oblique"]
    font_weight: Literal[
        "normal", "bold", "lighter", "bolder",
        "100", "200", "300", "400", "500", "600", "700", "800", "900"
    ]
    text_align: Literal["left", "right", "center", "justify", "start", "end"]
    text_transform: Literal["none", "uppercase", "lowercase", "capitalize", "full-width"]
    text_decoration: Literal["none", "underline", "line-through", "overline"]
    letter_spacing: Any
    line_height: Any
    white_space: Literal["normal", "nowrap", "pre", "pre-line", "pre-wrap"]

    # 📐 Alignment
    justify_content: Literal["start", "end", "center", "space-between", "space-around", "space-evenly"]
    justify_items: Literal["start", "end", "center", "baseline", "stretch"]
    align_content: Literal["start", "end", "center", "space-between", "space-around", "space-evenly"]
    align_items: Literal["start", "end", "center", "baseline", "stretch"]
    align_self: Literal["auto", "start", "end", "center", "stretch"]
    place_content: Literal["start", "end", "center", "space-between", "space-around"]
    place_items: Literal["start", "end", "center", "baseline", "stretch"]
    place_self: Literal["auto", "start", "end", "center", "stretch"]

    # 🧩 Miscellaneous
    break_after: Literal["auto", "all", "avoid", "slice", "column", "page", "recto", "verso"]
    break_before: Literal["auto", "all", "avoid", "slice", "column", "page", "recto", "verso"]
    break_inside: Literal["auto", "avoid", "slice"]
    cursor: Literal["pointer", "default", "text", "move", "not-allowed", "wait"]
    transition: str
    animation: str


StyleProps = Unpack[StylePropsDict]

Css: Optional[Mapping[str, str]] = None

# Allowed text alignment values
Align = Literal["left", "center", "right", "justify", "start", "end"]

# Allowed semantic font sizes
TextSize = Literal[
    "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"
]

# Allowed semantic font weights
FontWeight = Literal[
    "light", "normal", "medium", "semibold", "bold", "extrabold"
]

# Allowed HTML tag types for the <Text> component
Tag = Literal["div", "span", "p", "h1", "h2", "h3", "h4", "h5", "h6"]

__all__ = [StyleProps, Align, TextSize, FontWeight, Tag]
ContentLike = Union[str, Signal]
