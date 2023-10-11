from pweb import Blueprint, url_for
from pweb_auth.service.operator_ssr_service import OperatorSSRService
from pweb_ui.common.pweb_ui_config import PWebUIConfig

auth_controller: Blueprint = Blueprint(
    "auth_controller",
    __name__,
    url_prefix=PWebUIConfig.SSR_AUTH_END_POINT
)


operator_ssr_service = OperatorSSRService()


@auth_controller.route(PWebUIConfig.AUTH_BASE_END_POINT, methods=['GET'])
@auth_controller.route(PWebUIConfig.LOGIN_END_POINT, methods=['POST', 'GET'])
def login():
    success_redirect_url = url_for("operator_controller.list")
    return operator_ssr_service.login(view_name="auth/login", success_redirect_url=success_redirect_url)


@auth_controller.route(PWebUIConfig.LOGOUT_END_POINT, methods=['GET'])
def logout():
    logout_redirect_url = url_for("auth_controller.login")
    return operator_ssr_service.logout(logout_redirect_url=logout_redirect_url)


@auth_controller.route(f"{PWebUIConfig.RESET_PASS_END_POINT}/<string:token>", methods=['POST', 'GET'])
def reset_password(token: str):
    return operator_ssr_service.reset_password(view_name="auth/reset-password", reset_response_view="auth/reset-response", token=token)


@auth_controller.route(PWebUIConfig.FORGOT_PASS_END_POINT, methods=['POST', 'GET'])
def forgot_password():
    return operator_ssr_service.forgot_password(view_name="auth/forgot-password", forgot_response_view="auth/forgot-response")
