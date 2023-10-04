from pweb import PWebComponentRegister, PWebModuleDetails
from pweb_ui.common.pweb_ui_init import PWebUIInit


class PWebUIModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="pweb-ui", display_name="PWeb UI Module")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        PWebUIInit().init(pweb_app=pweb_app, config=config)

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pass
