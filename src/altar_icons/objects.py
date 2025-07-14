from aether.tags.svg import Circle, Line, Path, Rect

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


class LogInIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="m10 17 5-5-5-5"),
            Path(d="M15 12H3"),
            Path(d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"),
        ]


class LogOutIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="m16 17 5-5-5-5"),
            Path(d="M21 12H9"),
            Path(d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"),
        ]


class UserIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"),
            Circle(cx="12", cy="7", r="4"),
        ]


class UserPlusIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"),
            Circle(cx="9", cy="7", r="4"),
            Line(x1="19", x2="19", y1="8", y2="14"),
            Line(x1="22", x2="16", y1="11", y2="11"),
        ]


class MailIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"),
            Rect(width="20", height="16", x="2", y="4", rx="2", ry="2"),
        ]


class IdCardIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M16 10h2"),
            Path(d="M16 14h2"),
            Path(d="M6.17 15a3 3 0 0 1 5.66 0"),
            Circle(cx="9", cy="11", r="2"),
            Rect(width="20", height="14", x="2", y="5", rx="2", ry="2"),
        ]


class LockIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="18", height="11", x="3", y="11", rx="2", ry="2"),
            Path(d="M7 11V7a5 5 0 0 1 10 0v4"),
        ]


class LockQuestionMarkIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M20 11.8V12a2 2 0 0 0-2-1H5a2 2 0 0 0-2 2v7c0 1.1.9 2 2 2h11.5"),
            Path(
                d="M18 16c.2-.4.5-.8.9-1a2.1 2.1 0 0 1 2.6.4c.3.4.5.8.5 1.3 0 1.3-2 2-2 2"
            ),
            Path(d="M20 22v.01"),
            Path(d="M7 11V7a5 5 0 0 1 10 0v4"),
        ]


class KeyRoundIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"
            ),
            Circle(fill="currentColor", cx="16.5", cy="7.5", r=".5"),
        ]
