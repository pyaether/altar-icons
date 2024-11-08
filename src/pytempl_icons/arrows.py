from typing import Any, Dict

from pytempl.tags import Path, Svg


class ArrowLeftIcon(Svg):
    def __init__(self, **attributes: Dict[str, Any]):
        class_attribute = attributes.pop("_class", "")
        width = attributes.pop("width", "16")
        height = attributes.pop("height", "16")
        stroke_width = attributes.pop("stroke_width", "1.5")

        super().__init__(
            _class=class_attribute,
            width=width,
            height=height,
            viewBox="0 0 24 24",
            fill="none",
            stroke="currentColor",
            stroke_width=stroke_width,
            stroke_linecap="round",
            stroke_linejoin="round",
            **attributes,
        )

        self.children = [Path(d="M6 8L2 12L6 16"), Path(d="M2 12H22")]


class ArrowRightIcon(Svg):
    def __init__(self, **attributes: Dict[str, Any]):
        class_attribute = attributes.pop("_class", "")
        width = attributes.pop("width", "16")
        height = attributes.pop("height", "16")
        stroke_width = attributes.pop("stroke_width", "1.5")

        super().__init__(
            _class=class_attribute,
            width=width,
            height=height,
            viewBox="0 0 24 24",
            fill="none",
            stroke="currentColor",
            stroke_width=stroke_width,
            stroke_linecap="round",
            stroke_linejoin="round",
            **attributes,
        )

        self.children = [Path(d="M18 8L22 12L18 16"), Path(d="M2 12H22")]


class ChevronDownIcon(Svg):
    def __init__(self, **attributes: Dict[str, Any]):
        class_attribute = attributes.pop("_class", "")
        width = attributes.pop("width", "16")
        height = attributes.pop("height", "16")
        stroke_width = attributes.pop("stroke_width", "1.5")

        super().__init__(
            _class=class_attribute,
            width=width,
            height=height,
            viewBox="0 0 24 24",
            fill="none",
            stroke="currentColor",
            stroke_width=stroke_width,
            stroke_linecap="round",
            stroke_linejoin="round",
            **attributes,
        )

        self.children = [Path(d="m6 9 6 6 6-6")]


class ChevronLeftIcon(Svg):
    def __init__(self, **attributes: Dict[str, Any]):
        class_attribute = attributes.pop("_class", "")
        width = attributes.pop("width", "16")
        height = attributes.pop("height", "16")
        stroke_width = attributes.pop("stroke_width", "1.5")

        super().__init__(
            _class=class_attribute,
            width=width,
            height=height,
            viewBox="0 0 24 24",
            fill="none",
            stroke="currentColor",
            stroke_width=stroke_width,
            stroke_linecap="round",
            stroke_linejoin="round",
            **attributes,
        )

        self.children = [Path(d="m15 18-6-6 6-6")]


class ChevronRightIcon(Svg):
    def __init__(self, **attributes: Dict[str, Any]):
        class_attribute = attributes.pop("_class", "")
        width = attributes.pop("width", "16")
        height = attributes.pop("height", "16")
        stroke_width = attributes.pop("stroke_width", "1.5")

        super().__init__(
            _class=class_attribute,
            width=width,
            height=height,
            viewBox="0 0 24 24",
            fill="none",
            stroke="currentColor",
            stroke_width=stroke_width,
            stroke_linecap="round",
            stroke_linejoin="round",
            **attributes,
        )

        self.children = [Path(d="m9 18 6-6-6-6")]


class ChevronUpIcon(Svg):
    def __init__(self, **attributes: Dict[str, Any]):
        class_attribute = attributes.pop("_class", "")
        width = attributes.pop("width", "16")
        height = attributes.pop("height", "16")
        stroke_width = attributes.pop("stroke_width", "1.5")

        super().__init__(
            _class=class_attribute,
            width=width,
            height=height,
            viewBox="0 0 24 24",
            fill="none",
            stroke="currentColor",
            stroke_width=stroke_width,
            stroke_linecap="round",
            stroke_linejoin="round",
            **attributes,
        )

        self.children = [Path(d="m18 15-6-6-6 6")]
