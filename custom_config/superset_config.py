import os

# ---------------------------------------------------------
# 1. Configurações Básicas da Aplicação
# ---------------------------------------------------------
APP_NAME = "S4 ERP Analytics"
# APP_ICON = "/static/assets/logo.png"  # Descomentar quando tiver a logo
# FAVICONS = [{"href": "/static/assets/favicon.png"}]

# Desabilitar funcionalidades que não são "Enterprise Grade" ou necessárias
ENABLE_PROXY_FIX = True
ROW_LIMIT = 5000
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "MUDE_ESTA_CHAVE_EM_PROD")

# ---------------------------------------------------------
# Configuração do Banco de Dados (Metadados do Superset)
# ---------------------------------------------------------
# Use variáveis de ambiente para configurar um banco externo
# Exemplo PostgreSQL: postgresql://user:password@host:5432/superset
# Exemplo MySQL: mysql://user:password@host:3306/superset
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SUPERSET_DATABASE_URI",
    "sqlite:////app/superset_home/superset.db"  # Fallback para SQLite local
)

# ---------------------------------------------------------
# 2. Design System & Theme Overrides (Sem Rebuild)
# ---------------------------------------------------------
THEME_OVERRIDES = {
    "borderRadius": {
        "base": "8px",
        "m": "8px",
        "l": "12px",  # Para Cards
    },
    "colors": {
        "primary": {
            "base": "#0B7FC2",  # Azul Principal
            "dark1": "#0A6BA0",  # Azul Hover
            "light1": "#E8EDF2",
            "light2": "#F5F8FA",
        },
        "grayscale": {
            "dark1": "#1B2A3D",  # Azul Corporativo (Texto forte)
            "base": "#64748B",  # Cinza neutro
            "light1": "#E8EDF2",  # Bordas
            "light2": "#F5F8FA",  # Fundos off-white
            "light5": "#FFFFFF",  # Branco puro
        },
        "error": {
            "base": "#E04F5F",
        },
        "success": {
            "base": "#10B981",  # Verde Ação
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

# ---------------------------------------------------------
# 3. Paleta de Cores para Gráficos (Data Visualization)
# ---------------------------------------------------------
EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": "corporate_palette",
        "description": "Paleta Corporativa Oficial",
        "colors": [
            "#0B7FC2",  # Azul Principal
            "#1B2A3D",  # Azul Escuro
            "#10B981",  # Verde Ação
            "#64748B",  # Cinza Neutro
            "#F59E0B",  # Âmbar (Complementar sugerida)
            "#8B5CF6",  # Roxo (Complementar sugerida)
        ]
    }
]

# ---------------------------------------------------------
# 4. Injeção de CSS Customizado (Poppins + UI Fixes)
# ---------------------------------------------------------
# Como não estamos fazendo rebuild, precisamos injetar o CSS via configuração de dashboard
# ou template. Essa flag habilita o uso de CSS Templates no UI.
ENABLE_TEMPLATE_PROCESSING = True

# ---------------------------------------------------------
# 5. Feature Flags & Embedding Configuration
# ---------------------------------------------------------
# Habilita o uso de Jinja nas queries e RLS
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True
}

# Permite que o dashboard seja exibido dentro de um iframe do ERP
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'origins': ['https://app.s4erp.com/']  # URL do ERP
}

# Configuração de segurança obrigatória para Embedding (2026)
GUEST_ROLE_NAME = "Gamma"  # Papel base para usuários externos
GUEST_TOKEN_JWT_EXP_SECONDS = 3600  # 1 hora
