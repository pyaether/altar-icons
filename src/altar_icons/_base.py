from typing import Literal, NotRequired

from aether.tags.svg import Svg, SvgAttributes


class BaseSVGIconElement(Svg):
    pass


class SVGIconAttributes(SvgAttributes):
    _class: NotRequired[str]
    height: str
    fill: str | Literal["none"]
    stroke: str | Literal["none"]
    stroke_width: str
    stroke_linecap: Literal["butt", "round", "square"]
    stroke_linejoin: Literal["arcs", "bevel", "miter", "miter-clip", "round"]
    viewBox: str
    width: str

    @classmethod
    def set_defaults(cls) -> dict:
        return {
            "height": "16",
            "fill": "none",
            "stroke": "currentColor",
            "stroke_width": "1.5",
            "stroke_linecap": "round",
            "stroke_linejoin": "round",
            "viewBox": "0 0 24 24",
            "width": "16",
        }
