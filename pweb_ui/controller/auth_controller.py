from pweb import Blueprint
from pweb_form_rest import ssr_ui_render
from pweb_ui.common.pweb_ui_config import PWebUIConfig

auth_controller: Blueprint = Blueprint(
    "pweb-ui",
    __name__,
    url_prefix=PWebUIConfig.SSR_AUTH_END_POINT,
    template_folder="../template-assets/templates",
    static_folder="../template-assets/assets",
    static_url_path="pweb-ui-assets"
)


@auth_controller.route(PWebUIConfig.LOGIN_END_POINT, methods=['POST', 'GET'])
def login():
    return ssr_ui_render(view_name="auth/login")


@auth_controller.route(PWebUIConfig.LOGOUT_END_POINT, methods=['GET'])
def logout():
    pass


@auth_controller.route(f"{PWebUIConfig.RESET_PASS_END_POINT}/<string:token>", methods=['POST', 'GET'])
def reset_password(token: str):
    pass


@auth_controller.route(PWebUIConfig.FORGOT_PASS_END_POINT, methods=['POST', 'GET'])
def forgot_password():
    pass
