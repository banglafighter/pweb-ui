from flask import url_for
from pweb import Blueprint
from pweb_auth.service.operator_ssr_service import OperatorSSRService
from pweb_form_rest import ssr_ui_render

operator_controller: Blueprint = Blueprint(
    "operator_controller",
    __name__,
    url_prefix="/operator",
)

operator_ssr_service = OperatorSSRService()


@operator_controller.route("/create", methods=['POST', 'GET'])
def create():
    create_action_url = url_for("operator_controller.create")
    failed_redirect_url = url_for("operator_controller.list")
    return operator_ssr_service.create("operator/form", create_action_url=create_action_url, failed_redirect_url=failed_redirect_url)


@operator_controller.route("/list", methods=['GET'])
def list():
    return ssr_ui_render(view_name="operator/list")
