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
    LOGOUT_END_POINT: str = "/logout"
    RESET_PASS_END_POINT: str = "/reset-password"
    FORGOT_PASS_END_POINT: str = "/forgot-password"
    RENEW_TOKEN_END_POINT: str = "/renew-token"
