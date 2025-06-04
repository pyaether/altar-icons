from aether.tags.svg import Circle, Path, Rect

from ._base import BaseSVGIconElement, SVGIconAttributes

try:
    from typing import Unpack
except ImportError:
    from typing_extensions import Unpack


class EyeIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"
            ),
            Circle(cx="12", cy="12", r="3"),
        ]


class EyeOffIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49"
            ),
            Path(d="M14.084 14.158a3 3 0 0 1-4.242-4.242"),
            Path(
                d="M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143"
            ),
            Path(d="m2 2 20 20"),
        ]


class BanknoteIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="20", height="12", x="2", y="6", rx="2"),
            Circle(cx="12", cy="12", r="2"),
            Path(d="M6 12h.01M18 12h.01"),
        ]


class PencilIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"
            ),
            Path(d="m15 5 4 4"),
        ]


class TrashIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M3 6h18"),
            Path(d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"),
            Path(d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"),
        ]
