class PWebUIConfig:
    # API End Point
    ENABLE_OPERATOR_API: bool = False
    OPERATOR_API_END_POINT: str = "/api/vi/auth"

    # Form End Point
    ENABLE_SSR_AUTH: bool = True
    SSR_AUTH_END_POINT: str = "/auth"

    # End Point
    AUTH_BASE_END_POINT: str = "/"
    LOGIN_END_POINT: str = "/login"
    LOGIN_SUCCESS_END_POINT: str = None
    LOGOUT_END_POINT: str = "/logout"
    RESET_PASS_END_POINT: str = "/reset-password"
    FORGOT_PASS_END_POINT: str = "/forgot-password"
    RENEW_TOKEN_END_POINT: str = "/renew-token"
    REGISTRATION_END_POINT: str = "/registration"

    # Navigation
    LEFT_NAVIGATION: list = []  # It will be a list of map [{"name": "Student", "url": "/student", "icon": "font-awsome-icon-class"}]

    # Messages
    REGISTRATION_DISABLE_MESSAGE: str = "Registration is disabled."
    CONNECT_MESSAGE: str = "PWeb is an Open Source Python based Web Framework for Rapid Development."
    DEVELOPED_BY: str = "Bangla Fighter Engineering"
    DEVELOPED_BY_LINK: str = "https://banglafighter.com"
    APP_VERSION: str = "v1.0.0"
    ENABLE_REGISTRATION: bool = False
    REGISTRATION_ACTION: str = "auth_controller.login"
