from pweb import Blueprint
from pweb_ui.common.pweb_ui_config import PWebUIConfig

auth_controller: Blueprint = Blueprint("pweb-ui", __name__)


def init_auth_controller(url_prefix: str):
    global auth_controller
    auth_controller = Blueprint(
        "pweb-ui",
        __name__,
        url_prefix=url_prefix,
        template_folder="../template-assets/templates",
        static_folder="../template-assets/assets",
        static_url_path="pweb-ui-assets"
    )
    return auth_controller


@auth_controller.route(PWebUIConfig.LOGIN_END_POINT, methods=['POST', 'GET'])
def login():
    pass


@auth_controller.route(PWebUIConfig.LOGOUT_END_POINT, methods=['GET'])
def logout():
    pass


@auth_controller.route(f"{PWebUIConfig.RESET_PASS_END_POINT}/<string:token>", methods=['POST', 'GET'])
def reset_password(token: str):
    pass


@auth_controller.route(PWebUIConfig.FORGOT_PASS_END_POINT, methods=['POST', 'GET'])
def forgot_password():
    pass
