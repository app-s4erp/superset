import os
from flask import g

APP_NAME = "S4 ERP Analytics"
ENABLE_PROXY_FIX = True
ROW_LIMIT = 5000
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "MUDE_ESTA_CHAVE_EM_PROD")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SUPERSET_DATABASE_URI",
    "sqlite:////app/superset_home/superset.db"
)

THEME_OVERRIDES = {
    "borderRadius": {
        "base": "8px",
        "m": "8px",
        "l": "12px",
    },
    "colors": {
        "primary": {
            "base": "#0B7FC2",
            "dark1": "#0A6BA0",
            "light1": "#E8EDF2",
            "light2": "#F5F8FA",
        },
        "grayscale": {
            "dark1": "#1B2A3D",
            "base": "#64748B",
            "light1": "#E8EDF2",
            "light2": "#F5F8FA",
            "light5": "#FFFFFF",
        },
        "error": {
            "base": "#E04F5F",
        },
        "success": {
            "base": "#10B981",
        },
        "info": {
            "base": "#0B7FC2",
        },
    },
    "typography": {
        "fontFamily": "'Poppins', sans-serif",
        "sizes": {
            "s": "0.85rem",
            "m": "1rem",
            "l": "1.3rem",
            "xl": "2rem",
            "xxl": "2.5rem",
        },
        "weights": {
            "normal": 400,
            "bold": 700,
        },
    },
}

EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": "corporate_palette",
        "description": "Paleta Corporativa Oficial",
        "colors": [
            "#0B7FC2",
            "#1B2A3D",
            "#10B981",
            "#64748B",
            "#F59E0B",
            "#8B5CF6",
        ]
    }
]

ENABLE_TEMPLATE_PROCESSING = True

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True
}

HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'origins': ['https://app.s4erp.com/']
}

GUEST_ROLE_NAME = "Gamma"
GUEST_TOKEN_JWT_EXP_SECONDS = 3600

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
