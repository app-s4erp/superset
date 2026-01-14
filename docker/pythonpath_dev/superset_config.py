# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# This file is included in the final Docker image and SHOULD be overridden when
# deploying the image to prod. Settings configured here are intended for use in local
# development environments. Also note that superset_config_docker.py is imported
# as a final step as a means to override "defaults" configured here
#
import logging
import os
import sys

from celery.schedules import crontab
from flask_caching.backends.filesystemcache import FileSystemCache

logger = logging.getLogger()

DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

EXAMPLES_USER = os.getenv("EXAMPLES_USER")
EXAMPLES_PASSWORD = os.getenv("EXAMPLES_PASSWORD")
EXAMPLES_HOST = os.getenv("EXAMPLES_HOST")
EXAMPLES_PORT = os.getenv("EXAMPLES_PORT")
EXAMPLES_DB = os.getenv("EXAMPLES_DB")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = (
    f"{DATABASE_DIALECT}://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

# Use environment variable if set, otherwise construct from components
# This MUST take precedence over any other configuration
SQLALCHEMY_EXAMPLES_URI = os.getenv(
    "SUPERSET__SQLALCHEMY_EXAMPLES_URI",
    (
        f"{DATABASE_DIALECT}://"
        f"{EXAMPLES_USER}:{EXAMPLES_PASSWORD}@"
        f"{EXAMPLES_HOST}:{EXAMPLES_PORT}/{EXAMPLES_DB}"
    ),
)


REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG
THUMBNAIL_CACHE_CONFIG = CACHE_CONFIG

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

class CeleryConfig:
    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    imports = (
        "superset.sql_lab",
        "superset.tasks.scheduler",
        "superset.tasks.thumbnails",
        "superset.tasks.cache",
    )
    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    worker_prefetch_multiplier = 1
    task_acks_late = False
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
    }


CELERY_CONFIG = CeleryConfig

FEATURE_FLAGS = {"ALERT_REPORTS": True}
ALERT_REPORTS_NOTIFICATION_DRY_RUN = True
WEBDRIVER_BASEURL = f"http://superset_app{os.environ.get('SUPERSET_APP_ROOT', '/')}/"  # When using docker compose baseurl should be http://superset_nginx{ENV{BASEPATH}}/  # noqa: E501
# The base URL for the email report hyperlinks.
WEBDRIVER_BASEURL_USER_FRIENDLY = (
    f"http://localhost:8888/{os.environ.get('SUPERSET_APP_ROOT', '/')}/"
)
SQLLAB_CTAS_NO_LIMIT = True

log_level_text = os.getenv("SUPERSET_LOG_LEVEL", "INFO")
LOG_LEVEL = getattr(logging, log_level_text.upper(), logging.INFO)

if os.getenv("CYPRESS_CONFIG") == "true":
    # When running the service as a cypress backend, we need to import the config
    # located @ tests/integration_tests/superset_test_config.py
    base_dir = os.path.dirname(__file__)
    module_folder = os.path.abspath(
        os.path.join(base_dir, "../../tests/integration_tests/")
    )
    sys.path.insert(0, module_folder)
    from superset_test_config import *  # noqa

    sys.path.pop(0)

#
# Optionally import superset_config_docker.py (which will have been included on
# the PYTHONPATH) in order to allow for local settings to be overridden
#
try:
    import superset_config_docker
    from superset_config_docker import *  # noqa: F403

    logger.info(
        "Loaded your Docker configuration at [%s]", superset_config_docker.__file__
    )
except ImportError:
    logger.info("Using default Docker config...")
