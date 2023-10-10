from pweb import Blueprint
from pweb_auth.form_dto.pweb_auth_dto import LoginEmailBaseDefaultDTO, LoginResponseDefaultDTO, ResetPasswordDefaultDTO, \
    ForgotPasswordEmailBaseDefaultDTO, RefreshTokenDefaultDTO, LoginTokenDefaultDTO
from pweb_auth.service.operator_api_service import OperatorAPIService
from pweb_form_rest import pweb_endpoint
from pweb_ui.common.pweb_ui_config import PWebUIConfig

auth_api_controller: Blueprint = Blueprint(
    "auth_api_controller",
    __name__,
    url_prefix=PWebUIConfig.OPERATOR_API_END_POINT,
)

operator_api_service = OperatorAPIService()


@auth_api_controller.route(PWebUIConfig.LOGIN_END_POINT, methods=['POST'])
@pweb_endpoint(request_obj=LoginEmailBaseDefaultDTO, response_obj=LoginResponseDefaultDTO)
def login():
    return operator_api_service.login()


@auth_api_controller.route(PWebUIConfig.LOGOUT_END_POINT, methods=['GET'])
@pweb_endpoint(pweb_message_response=True)
def logout():
    return operator_api_service.logout()


@auth_api_controller.route(f"{PWebUIConfig.RESET_PASS_END_POINT}", methods=['POST'])
@pweb_endpoint(request_obj=ResetPasswordDefaultDTO, pweb_message_response=True)
def reset_password():
    return operator_api_service.reset_password()


@auth_api_controller.route(PWebUIConfig.FORGOT_PASS_END_POINT, methods=['POST'])
@pweb_endpoint(request_obj=ForgotPasswordEmailBaseDefaultDTO, pweb_message_response=True)
def forgot_password():
    return operator_api_service.forgot_password()


@auth_api_controller.route(PWebUIConfig.RENEW_TOKEN_END_POINT, methods=['POST'])
@pweb_endpoint(request_obj=RefreshTokenDefaultDTO, response_obj=LoginTokenDefaultDTO)
def renew_token():
    return operator_api_service.renew_token()
