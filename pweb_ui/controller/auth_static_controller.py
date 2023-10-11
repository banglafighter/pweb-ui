from pweb import Blueprint

auth_static_controller: Blueprint = Blueprint(
    "pweb-ui",
    __name__,
    url_prefix="/",
    template_folder="../template-assets/templates",
    static_folder="../template-assets/assets",
    static_url_path="pweb-ui-assets"
)
