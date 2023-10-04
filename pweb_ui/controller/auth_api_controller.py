from pweb import Blueprint
from pweb_ui.common.pweb_ui_config import PWebUIConfig

auth_api_controller: Blueprint = Blueprint(
    "auth_api_controller",
    __name__,
    url_prefix=PWebUIConfig.SSR_AUTH_END_POINT,
)


@auth_api_controller.route(PWebUIConfig.LOGIN_END_POINT, methods=['POST'])
def login():
    pass


@auth_api_controller.route(PWebUIConfig.LOGOUT_END_POINT, methods=['GET'])
def logout():
    pass


@auth_api_controller.route(f"{PWebUIConfig.RESET_PASS_END_POINT}/<string:token>", methods=['GET'])
def reset_password(token: str):
    pass


@auth_api_controller.route(PWebUIConfig.FORGOT_PASS_END_POINT, methods=['POST'])
def forgot_password():
    pass
