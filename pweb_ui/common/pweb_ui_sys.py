from pweb_ssr import PWebJinjaUtil


class PWebUISys:
    PWEB_INSTANCE = None
    LEFT_NAVIGATION: list = []
    ENABLE_DEFAULT_LEFT_NAV: bool = True

    @staticmethod
    def add_to_nav(name: str, url: str, icon_class: str = ""):
        PWebUISys.LEFT_NAVIGATION.append({
            "name": name, "url": url, "icon": icon_class
        })
        if PWebUISys.PWEB_INSTANCE:
            PWebUISys.register_left_nav(PWebUISys.PWEB_INSTANCE, PWebUISys.LEFT_NAVIGATION)

    @staticmethod
    def clear_left_nav():
        PWebUISys.LEFT_NAVIGATION = []
        if PWebUISys.PWEB_INSTANCE:
            PWebUISys.register_left_nav(PWebUISys.PWEB_INSTANCE, PWebUISys.LEFT_NAVIGATION)

    @staticmethod
    def register_left_nav(pweb_app, navigation_list: list = None):
        if not navigation_list:
            navigation_list = PWebUISys.LEFT_NAVIGATION
        PWebJinjaUtil.register_global_variable(pweb_app, {"navigation": navigation_list}, is_update=True)
