from typing import Any, Dict

from pytempl.tags import Circle, Line, Path, Svg


class CheckIcon(Svg):
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

        self.children = [Path(d="M20 6 9 17l-5-5")]


class CheckCircleBigIcon(Svg):
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

        self.children = [
            Path(d="M21.801 10A10 10 0 1 1 17 3.335"),
            Path(d="m9 11 3 3L22 4"),
        ]


class CrossIcon(Svg):
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

        self.children = [Path(d="M18 6 6 18"), Path(d="m6 6 12 12")]


class DotFilledIcon(Svg):
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

        self.children = [Circle(cx="12.1", cy="12.1", r="1")]


class ExclamationTriangleIcon(Svg):
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

        self.children = [
            Path(
                d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"
            ),
            Path(d="M12 9v4"),
            Path(d="M12 17h.01"),
        ]


class PlusIcon(Svg):
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

        self.children = [Path(d="M5 12h14"), Path(d="M12 5v14")]


class CirclePlusIcon(Svg):
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

        self.children = [
            Circle(cx="12", cy="12", r="10"),
            Path(d="M8 12h8"),
            Path(d="M12 8v8"),
        ]


class RefreshCWIcon(Svg):
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

        self.children = [
            Path(d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"),
            Path(d="M21 3v5h-5"),
            Path(d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"),
            Path(d="M8 16H3v5"),
        ]


class HamburgerMenuIcon(Svg):
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

        self.children = [
            Line(x1="4", x2="20", y1="12", y2="12"),
            Line(x1="4", x2="20", y1="6", y2="6"),
            Line(x1="4", x2="20", y1="18", y2="18"),
        ]


class EllipsisIcon(Svg):
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

        self.children = [
            Circle(cx="12", cy="12", r="1"),
            Circle(cx="19", cy="12", r="1"),
            Circle(cx="5", cy="12", r="1"),
        ]


class LoaderCircleIcon(Svg):
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

        self.children = [Path(d="M21 12a9 9 0 1 1-6.219-8.56")]
