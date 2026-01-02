from aether.tags.svg import Path

from ._base import BaseSVGIconElement, SVGIconAttributes

try:
    from typing import Unpack
except ImportError:
    from typing_extensions import Unpack


class ArrowLeftIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="m12 19-7-7 7-7"), Path(d="M19 12H5")]


class ArrowRightIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M5 12h14"), Path(d="m12 5 7 7-7 7")]


class ArrowDownIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M12 5v14"), Path(d="m19 12-7 7-7-7")]


class ArrowUpIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="m5 12 7-7 7 7"), Path(d="M12 19V5")]


class ArrowDownLeftIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M17 7 7 17"), Path(d="M17 17H7V7")]


class ArrowUpRightIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M7 7h10v10"), Path(d="M7 17 17 7")]


class MoveDownIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M8 18L12 22L16 18"), Path(d="M12 2V22")]


class MoveLeftIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M6 8L2 12L6 16"), Path(d="M2 12H22")]


class MoveRightIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M18 8L22 12L18 16"), Path(d="M2 12H22")]


class MoveUpIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M8 6L12 2L16 6"), Path(d="M12 2V22")]


class TrendingDownIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M16 17h6v-6"), Path(d="m22 17-8.5-8.5-5 5L2 7")]


class TrendingUpIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="M16 7h6v6"), Path(d="m22 7-8.5 8.5-5-5L2 17")]


class ChevronDownIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="m6 9 6 6 6-6")]


class ChevronLeftIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="m15 18-6-6 6-6")]


class ChevronRightIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="m9 18 6-6-6-6")]


class ChevronUpIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [Path(d="m18 15-6-6-6 6")]


class MoveHorizontalIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="m18 8 4 4-4 4"),
            Path(d="M2 12h20"),
            Path(d="m6 8-4 4 4 4"),
        ]
