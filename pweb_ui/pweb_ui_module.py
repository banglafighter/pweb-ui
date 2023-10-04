from pweb import PWebComponentRegister, PWebModuleDetails
from pweb_ui.controller.auth_api_controller import auth_api_controller
from pweb_ui.controller.auth_controller import auth_controller


class PWebUIModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-ui", display_name="PWeb UI Module")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(auth_controller)
        pweb_app.register_blueprint(auth_api_controller)
