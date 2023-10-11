from pweb import PWebComponentRegister, PWebModuleDetails, url_for
from pweb_auth import PWebAuthRegistry
from pweb_form_rest import PWebFRConfig
from pweb_ui.common.pweb_ui_config import PWebUIConfig
from pweb_ui.controller.auth_api_controller import auth_api_controller
from pweb_ui.controller.auth_controller import auth_controller
from pweb_ui.controller.auth_static_controller import auth_static_controller
from pweb_ui.controller.operator_controller import operator_controller


class PWebUIModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-ui", display_name="PWeb UI Module")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        PWebAuthRegistry.add_start_with_url_in_skip("/pweb-ui-assets")
        PWebAuthRegistry.add_start_with_url_in_skip(PWebUIConfig.OPERATOR_API_END_POINT)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebUIConfig.SSR_AUTH_END_POINT)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_JSON_URL)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_UI_URL)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_UI_ASSETS_URL)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_UI_ASSETS_URL)

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(auth_static_controller)
        pweb_app.register_blueprint(auth_controller)
        pweb_app.register_blueprint(auth_api_controller)
        pweb_app.register_blueprint(operator_controller)
