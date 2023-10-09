from flask import url_for
from pweb import Blueprint
from pweb_auth.service.operator_ssr_service import OperatorSSRService

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


@operator_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int):
    update_action_url = url_for("operator_controller.update", id=id)
    failed_redirect_url = url_for("operator_controller.list")
    return operator_ssr_service.update("operator/form", update_action_url=update_action_url, failed_redirect_url=failed_redirect_url, model_id=id)


@operator_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    redirect_url = url_for("operator_controller.list")
    return operator_ssr_service.delete(model_id=id, redirect_url=redirect_url)


@operator_controller.route("/details/<int:id>", methods=['GET'])
def details(id: int):
    redirect_url = url_for("operator_controller.list")
    return operator_ssr_service.details(view_name="operator/details", model_id=id, redirect_url=redirect_url)


@operator_controller.route("/", methods=['GET'])
@operator_controller.route("/list", methods=['GET'])
def list():
    search_fields: list = ["name", "email", "username"]
    return operator_ssr_service.list(view_name="operator/list", search_fields=search_fields)
