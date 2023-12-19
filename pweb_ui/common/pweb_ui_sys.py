from pweb_auth.security.pweb_session import PWebSession
from pweb_ssr import PWebJinjaUtil


class PWebUISys:
    PWEB_INSTANCE = None
    PWEB_NAV_NAME = "PWEB_NAV_NAME"
    ENABLE_DEFAULT_LEFT_NAV: bool = True

    @staticmethod
    def add_to_nav(name: str, url: str, icon_class: str = ""):
        left_navigation: list = PWebSession.get(PWebUISys.PWEB_NAV_NAME, [])
        left_navigation.append({"name": name, "url": url, "icon": icon_class})
        if PWebUISys.PWEB_INSTANCE:
            PWebUISys.register_left_nav(PWebUISys.PWEB_INSTANCE, left_navigation)
        PWebSession.add(PWebUISys.PWEB_NAV_NAME, left_navigation)

    @staticmethod
    def clear_left_nav():
        left_navigation = []
        PWebSession.add(PWebUISys.PWEB_NAV_NAME, left_navigation)
        if PWebUISys.PWEB_INSTANCE:
            PWebUISys.register_left_nav(PWebUISys.PWEB_INSTANCE, left_navigation)

    @staticmethod
    def register_left_nav(pweb_app, navigation_list: list = None):
        if not navigation_list:
            navigation_list: list = PWebSession.get(PWebUISys.PWEB_NAV_NAME, [])
        PWebJinjaUtil.register_global_variable(pweb_app, {"navigation": navigation_list}, is_update=True)
