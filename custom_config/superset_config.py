import os
from flask import g

APP_NAME = "S4 ERP Analytics"
ENABLE_PROXY_FIX = True
ROW_LIMIT = 5000
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "MUDE_ESTA_CHAVE_EM_PROD")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SUPERSET_DATABASE_URI",
    "sqlite:////app/superset_home/superset.db",
)

ENABLE_TEMPLATE_PROCESSING = True

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_RBAC": True,
}

GUEST_ROLE_NAME = "Admin"
GUEST_TOKEN_JWT_SECRET = os.getenv("GUEST_TOKEN_JWT_SECRET", "MUDE_ESTA_CHAVE_EM_PROD")
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_JWT_EXP_SECONDS = 3600

ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "resources": ["*"],
    "origins": [
        "https://app.s4erp.com",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
    "allow_headers": ["*"],
}

CONTENT_SECURITY_POLICY = {
    "default-src": ["'self'"],
    "img-src": ["'self'", "data:", "blob:"],
    "worker-src": ["'self'", "blob:"],
    "connect-src": ["'self'", "https:", "http:", "ws:", "wss:"],
    "style-src": ["'self'", "'unsafe-inline'", "https:"],
    "script-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'", "https:"],
    "font-src": ["'self'", "data:", "https:"],
    "frame-ancestors": [
        "https://app.s4erp.com",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
}

def current_user_email():
    try:
        if g.user and g.user.email:
            return g.user.email
        return ""
    except Exception:
        return ""

def current_user_id():
    try:
        if g.user and g.user.id:
            return g.user.id
        return None
    except Exception:
        return None

def current_username():
    try:
        if g.user and g.user.username:
            return g.user.username
        return ""
    except Exception:
        return ""

JINJA_CONTEXT_ADDONS = {
    "current_user_email": current_user_email,
    "current_user_id": current_user_id,
    "current_username": current_username,
}
