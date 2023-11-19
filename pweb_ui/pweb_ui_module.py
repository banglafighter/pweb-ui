from ppy_common import ObjectHelper
from pweb import PWebComponentRegister, PWebModuleDetails
import pweb_ui
from pweb_auth import PWebAuthRegistry
from pweb_form_rest import PWebFRConfig
from pweb_ssr import PWebJinjaUtil
from pweb_ui.common.pweb_ui_config import PWebUIConfig
from pweb_ui.controller.auth_api_controller import auth_api_controller
from pweb_ui.controller.auth_controller import auth_controller
from pweb_ui.controller.operator_controller import operator_controller
from pweb_ui.controller.pweb_ui_static_controller import pweb_ui_static_controller


class PWebUIModule(PWebComponentRegister):

    def register_global_variables(self, pweb_app):
        variables = {
            "CONNECT_MESSAGE": PWebUIConfig.CONNECT_MESSAGE,
            "DEVELOPED_BY": PWebUIConfig.DEVELOPED_BY,
            "DEVELOPED_BY_LINK": PWebUIConfig.DEVELOPED_BY_LINK,
            "APP_VERSION": PWebUIConfig.APP_VERSION,
            "ENABLE_REGISTRATION": PWebUIConfig.ENABLE_REGISTRATION,
        }
        PWebJinjaUtil.register_global_variable(pweb_app, variables)

        navigation = []
        if PWebUIConfig.LEFT_NAVIGATION:
            navigation = PWebUIConfig.LEFT_NAVIGATION
        PWebJinjaUtil.register_global_variable(pweb_app, {"navigation": navigation})

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-ui", display_name="PWeb UI Module")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        ObjectHelper.copy_config_property(config, pweb_ui.common.pweb_ui_config.PWebUIConfig)
        PWebAuthRegistry.add_start_with_url_in_skip("/pweb-ui-assets")
        PWebAuthRegistry.add_start_with_url_in_skip(PWebUIConfig.OPERATOR_API_END_POINT)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebUIConfig.SSR_AUTH_END_POINT)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_JSON_URL)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_UI_URL)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_UI_ASSETS_URL)
        PWebAuthRegistry.add_start_with_url_in_skip(PWebFRConfig.SWAGGER_UI_ASSETS_URL)
        self.register_global_variables(pweb_app)

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(pweb_ui_static_controller)
        pweb_app.register_blueprint(auth_controller)
        pweb_app.register_blueprint(auth_api_controller)
        pweb_app.register_blueprint(operator_controller)
