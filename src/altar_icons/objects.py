from aether.tags.svg import Circle, Ellipse, Line, Path, Rect

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


class GavelIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="m14 13-8.381 8.38a1 1 0 0 1-3.001-3l8.384-8.381"),
            Path(d="m16 16 6-6"),
            Path(d="m21.5 10.5-8-8"),
            Path(d="m8 8 6-6"),
            Path(d="m8.5 7.5 8 8"),
        ]


class BotIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M12 8V4H8"),
            Rect(width="16", height="12", x="4", y="8", rx="2", ry="2"),
            Path(d="M2 14h2"),
            Path(d="M20 14h2"),
            Path(d="M15 13v2"),
            Path(d="M9 13v2"),
        ]


class SlidersVerticalIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M10 8h4"),
            Path(d="M12 21v-9"),
            Path(d="M12 8V3"),
            Path(d="M17 16h4"),
            Path(d="M19 12V3"),
            Path(d="M19 21v-5"),
            Path(d="M3 14h4"),
            Path(d="M5 10V3"),
            Path(d="M5 21v-7"),
        ]


class NetworkIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="6", height="6", x="16", y="16", rx="1", ry="1"),
            Rect(width="6", height="6", x="2", y="16", rx="1", ry="1"),
            Rect(width="6", height="6", x="9", y="2", rx="1", ry="1"),
            Path(d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"),
            Path(d="M12 12V8"),
        ]


class BanknoteIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="20", height="12", x="2", y="6", rx="2", ry="2"),
            Circle(cx="12", cy="12", r="2"),
            Path(d="M6 12h.01M18 12h.01"),
        ]


class GlobeIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Circle(cx="12", cy="12", r="10"),
            Path(d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"),
            Path(d="M2 12h20"),
        ]


class CpuIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M12 20v2"),
            Path(d="M12 2v2"),
            Path(d="M17 20v2"),
            Path(d="M17 2v2"),
            Path(d="M2 12h2"),
            Path(d="M2 17h2"),
            Path(d="M2 7h2"),
            Path(d="M20 12h2"),
            Path(d="M20 17h2"),
            Path(d="M20 7h2"),
            Path(d="M7 20v2"),
            Path(d="M7 2v2"),
            Rect(width="16", height="16", x="4", y="4", rx="2", ry="2"),
            Rect(width="8", height="8", x="8", y="8", rx="1", ry="2"),
        ]


class FingerprintIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M12 10a2 2 0 0 0-2 2c0 1.02-.1 2.51-.26 4"),
            Path(d="M14 13.12c0 2.38 0 6.38-1 8.88"),
            Path(d="M17.29 21.02c.12-.6.43-2.3.5-3.02"),
            Path(d="M2 12a10 10 0 0 1 18-6"),
            Path(d="M2 16h.01"),
            Path(d="M21.8 16c.2-2 .131-5.354 0-6"),
            Path(d="M5 19.5C5.5 18 6 15 6 12a6 6 0 0 1 .34-2"),
            Path(d="M8.65 22c.21-.66.45-1.32.57-2"),
            Path(d="M9 6.8a6 6 0 0 1 9 5.2v2"),
        ]


class BrainCircuitIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"
            ),
            Path(d="M9 13a4.5 4.5 0 0 0 3-4"),
            Path(d="M6.003 5.125A3 3 0 0 0 6.401 6.5"),
            Path(d="M3.477 10.896a4 4 0 0 1 .585-.396"),
            Path(d="M6 18a4 4 0 0 1-1.967-.516"),
            Path(d="M12 13h4"),
            Path(d="M12 18h6a2 2 0 0 1 2 2v1"),
            Path(d="M12 8h8"),
            Path(d="M16 8V5a2 2 0 0 1 2-2"),
            Circle(cx="16", cy="13", r="0.5"),
            Circle(cx="18", cy="3", r="0.5"),
            Circle(cx="20", cy="21", r="0.5"),
            Circle(cx="20", cy="8", r="0.5"),
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


class UsersIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"),
            Path(d="M16 3.128a4 4 0 0 1 0 7.744"),
            Path(d="M22 21v-2a4 4 0 0 0-3-3.87"),
            Circle(cx="9", cy="7", r="4"),
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


class ServerIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="20", height="8", x="2", y="2", rx="2", ry="2"),
            Rect(width="20", height="8", x="2", y="14", rx="2", ry="2"),
            Line(x1="6", x2="6.01", y1="6", y2="6"),
            Line(x1="6", x2="6.01", y1="18", y2="18"),
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


class LockRotateIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="8", height="6", x="8", y="10.75", rx="1", ry="1"),
            Path(d="M10 10.25v-2a2 2 0 1 1 4 0v2"),
            Path(d="M3 12a9 9 0 1 0 9-9 9.74 9.74 0 0 0-6.74 2.74L3 8"),
            Path(d="M3 4v4h4"),
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


class KeyRotateIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="m14.5 9.5 1 1"),
            Path(d="m15.5 8.5-4 4"),
            Path(d="M3 12a9 9 0 1 0 9-9 9.74 9.74 0 0 0-6.74 2.74L3 8"),
            Path(d="M3 3v5h5"),
            Circle(cx="10", cy="14", r="2"),
        ]


class PanelLeftIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="18", height="18", x="3", y="3", rx="2", ry="2"),
            Path(d="M9 3v18"),
        ]


class PanelRightIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="18", height="18", x="3", y="3", rx="2", ry="2"),
            Path(d="M15 3v18"),
        ]


class WebsiteIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="20", height="16", x="2", y="4", rx="2", ry="2"),
            Circle(cx="5", cy="6.5", r="0.05"),
            Circle(cx="8", cy="6.5", r="0.05"),
            Circle(cx="11", cy="6.5", r="0.05"),
            Circle(cx="12", cy="13.5", r="4.75"),
            Path(d="M12 9.5a5 5 0 0 0 0 8 5 5 0 0 0 0-8"),
            Path(d="M8 13.5h8"),
        ]


class WebsitesIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="17", height="15", x="5", y="3", rx="2", ry="2"),
            Circle(cx="8", cy="5.5", r="0.05"),
            Circle(cx="11", cy="5.5", r="0.05"),
            Circle(cx="14", cy="5.5", r="0.05"),
            Circle(cx="13.5", cy="12", r="4"),
            Path(d="M13.5 8.5a6 5 0 0 0 0 7 6 5 0 0 0 0-7"),
            Path(d="M9.5 12h8"),
            Path(d="M2.5 8v11.5a2 2 0 0 0 2 1h14"),
        ]


class SettingsIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"
            ),
            Circle(cx="12", cy="12", r="3"),
        ]


class DatabaseIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Ellipse(cx="12", cy="5", rx="9", ry="3"),
            Path(d="M3 5V19A9 3 0 0 0 21 19V5"),
            Path(d="M3 12A9 3 0 0 0 21 12"),
        ]


class BookOpenIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M12 7v14"),
            Path(
                d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"
            ),
        ]


class FileIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"),
            Path(d="M14 2v4a2 2 0 0 0 2 2h4"),
        ]


class FileTextIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"),
            Path(d="M14 2v4a2 2 0 0 0 2 2h4"),
            Path(d="M10 9H8"),
            Path(d="M16 13H8"),
            Path(d="M16 17H8"),
        ]


class FolderIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"
            )
        ]


class MessageSquareIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z"
            )
        ]


class Share2Icon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Circle(cx="18", cy="5", r="3"),
            Circle(cx="6", cy="12", r="3"),
            Circle(cx="18", cy="19", r="3"),
            Line(x1="8.59", x2="15.42", y1="13.51", y2="17.49"),
            Line(x1="15.41", x2="8.59", y1="6.51", y2="10.49"),
        ]


class ExternalLinkIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M15 3h6v6"),
            Path(d="M10 14 21 3"),
            Path(d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"),
        ]


class TargetIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Circle(cx="12", cy="12", r="10"),
            Circle(cx="12", cy="12", r="6"),
            Circle(cx="12", cy="12", r="2"),
        ]


class CopyIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Rect(width="14", height="14", x="8", y="8", rx="2", ry="2"),
            Path(d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"),
        ]


class SendHorizontalIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(
                d="M3.714 3.048a.498.498 0 0 0-.683.627l2.843 7.627a2 2 0 0 1 0 1.396l-2.842 7.627a.498.498 0 0 0 .682.627l18-8.5a.5.5 0 0 0 0-.904z"
            ),
            Path(d="M6 12h16"),
        ]


class MicIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M12 19v3"),
            Path(d="M19 10v2a7 7 0 0 1-14 0v-2"),
            Rect(width="2", height="13", x="9", y="2", rx="3", ry="3"),
        ]


class CalendarIcon(BaseSVGIconElement):
    def __init__(self, **attributes: Unpack[SVGIconAttributes]):
        attributes_with_defaults = {**SVGIconAttributes.set_defaults(), **attributes}

        super().__init__(**attributes_with_defaults)

        self.children = [
            Path(d="M8 2v4"),
            Path(d="M16 2v4"),
            Rect(width="18", height="18", x="3", y="4", rx="2", ry="2"),
            Path(d="M3 10h18"),
        ]
