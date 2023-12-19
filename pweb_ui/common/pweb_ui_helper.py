from pweb_auth.security.pweb_session import PWebSession
from pweb_form_rest import PWebSSRUIHelper
from pweb_auth.security.pweb_ssr_auth import PWebSSRAuth
from pweb import url_for
from pweb_auth.service.operator_ssr_service import OperatorSSRService
from pweb_ui.common.pweb_ui_sys import PWebUISys


class AuthSessionHelper:
    pweb_ssr_auth = PWebSSRAuth()
    operator_ssr_service = OperatorSSRService()

    @property
    def name(self):
        name = "Unknown User"
        if self.pweb_ssr_auth.get_auth_session().name:
            name = self.pweb_ssr_auth.get_auth_session().name
        return name

    @property
    def title(self):
        title = "Unknown Title"
        if self.pweb_ssr_auth.get_auth_session().title:
            title = self.pweb_ssr_auth.get_auth_session().title
        return title

    def get_profile_photo(self, member=None):
        image_name = url_for('pweb-ui.static', filename='img/default-img.jpg')
        if not member:
            member = self.pweb_ssr_auth.get_auth_session()
        if member.profilePhoto:
            image_name = f"/assets/profile/{member.profilePhoto}"
        return image_name

    @property
    def profile_photo(self):
        return self.get_profile_photo()

    @property
    def navigation(self):
        return PWebSession.get(PWebUISys.PWEB_NAV_NAME, [])


class PWebUIHelper(PWebSSRUIHelper):

    def get_helper(self) -> dict:
        return {"auth": AuthSessionHelper()}
