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

EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": "s4_corporate",
        "description": "S4 ERP Analytics - Paleta Corporativa",
        "label": "S4 Corporate",
        "colors": [
            "#0B7FC2",
            "#10B981",
            "#1B2A3D",
            "#F59E0B",
            "#8B5CF6",
            "#64748B",
            "#06B6D4",
            "#EC4899",
        ]
    }
]

from superset.app import SupersetAppInitializer

class CustomSupersetAppInitializer(SupersetAppInitializer):
    def init_app_in_ctx(self):
        super().init_app_in_ctx()
        
        from flask import Markup
        
        custom_css = """
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
           * {
                font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
            }
            body,
            #app,
            .ant-layout,
            .dashboard,
            .dashboard-content,
            .main-container {
                background-color: #F5F8FA !important;
                color: #1B2A3D !important;
            }
            
            .header,
            .navbar,
            .ant-layout-header,
            .dashboard-header,
            .top-nav {
                background-color: #FFFFFF !important;
                border-bottom: 1px solid #E2E8F0 !important;
                box-shadow: 0 1px 3px rgba(27, 42, 61, 0.04) !important;
            }
            
            .navbar-brand {
                color: #0B7FC2 !important;
                font-weight: 700 !important;
            }
            
            .ant-layout-sider,
            .ant-menu,
            .menu,
            aside {
                background-color: #FFFFFF !important;
                border-right: 1px solid #E2E8F0 !important;
            }
            
            .ant-menu-item,
            .ant-menu-submenu-title {
                color: #64748B !important;
                border-radius: 8px !important;
                margin: 4px 8px !important;
            }
            
            .ant-menu-item-selected,
            .ant-menu-item-active,
            .ant-menu-item:hover {
                background-color: #E8F4FB !important;
                color: #0B7FC2 !important;
            }
            
            .ant-menu-item-selected::after {
                border-right-color: #0B7FC2 !important;
            }
            
            h1, h2, h3, h4, h5, h6,
            .header-title,
            .dashboard-title,
            .panel-title,
            .modal-title,
            .ant-modal-title,
            .ant-typography-title {
                color: #1B2A3D !important;
                font-weight: 600 !important;
            }
            
            h1 { font-size: 2rem !important; font-weight: 700 !important; }
            h2 { font-size: 1.5rem !important; }
            h3 { font-size: 1.25rem !important; }
            
            .dashboard-component-chart-holder,
            .chart-container,
            .slice_container,
            .ant-card,
            .panel,
            .widget {
                background-color: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
                border-radius: 12px !important;
                box-shadow: 0 1px 3px rgba(27, 42, 61, 0.04) !important;
                transition: box-shadow 0.3s ease, transform 0.2s ease;
            }
            
            .dashboard-component-chart-holder:hover,
            .chart-container:hover,
            .ant-card:hover {
                box-shadow: 0 4px 12px rgba(27, 42, 61, 0.08) !important;
                transform: translateY(-2px);
            }
            
            .ant-btn-primary,
            .btn-primary,
            button[type="submit"],
            .superset-button-primary {
                background-color: #0B7FC2 !important;
                border-color: #0B7FC2 !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
                color: #FFFFFF !important;
                box-shadow: 0 1px 2px rgba(11, 127, 194, 0.2) !important;
                transition: all 0.2s ease;
            }
            
            .ant-btn-primary:hover,
            .btn-primary:hover {
                background-color: #0A6BA0 !important;
                border-color: #0A6BA0 !important;
                box-shadow: 0 4px 8px rgba(11, 127, 194, 0.3) !important;
                transform: translateY(-1px);
            }
            
            .ant-btn-default,
            .btn-default {
                border-color: #E2E8F0 !important;
                border-radius: 8px !important;
                font-weight: 500 !important;
            }
            
            .ant-btn-default:hover {
                border-color: #0B7FC2 !important;
                color: #0B7FC2 !important;
            }
            
            .ant-btn-success,
            .btn-success {
                background-color: #10B981 !important;
                border-color: #10B981 !important;
                border-radius: 8px !important;
            }
            
            .ant-btn-success:hover {
                background-color: #059669 !important;
            }
            
            a {
                color: #0B7FC2 !important;
                transition: color 0.2s;
            }
            
            a:hover {
                color: #0A6BA0 !important;
                text-decoration: none !important;
            }
            
            .ant-tabs-tab {
                font-weight: 500 !important;
                color: #64748B !important;
                border-radius: 8px 8px 0 0 !important;
            }
            
            .ant-tabs-tab-active {
                color: #0B7FC2 !important;
                font-weight: 600 !important;
            }
            
            .ant-tabs-ink-bar {
                background-color: #0B7FC2 !important;
                height: 3px !important;
            }
            
            .ant-input,
            .ant-input-number,
            .ant-select-selector,
            .ant-picker,
            input[type="text"],
            input[type="email"],
            input[type="password"],
            textarea,
            select {
                border-radius: 8px !important;
                border-color: #E2E8F0 !important;
                transition: all 0.2s ease;
            }
            
            .ant-input:focus,
            .ant-select-focused .ant-select-selector,
            .ant-picker-focused,
            input:focus,
            textarea:focus {
                border-color: #0B7FC2 !important;
                box-shadow: 0 0 0 2px rgba(11, 127, 194, 0.1) !important;
            }
            
            .ant-modal-content,
            .modal-content {
                border-radius: 12px !important;
                box-shadow: 0 8px 32px rgba(27, 42, 61, 0.15) !important;
            }
            
            .ant-modal-header,
            .modal-header {
                border-bottom: 1px solid #E2E8F0 !important;
                border-radius: 12px 12px 0 0 !important;
                background-color: #F8FAFC !important;
            }
            
            .ant-modal-footer,
            .modal-footer {
                border-top: 1px solid #E2E8F0 !important;
                border-radius: 0 0 12px 12px !important;
            }
            
            .ant-table,
            .table,
            .dataTable {
                border-radius: 8px !important;
                overflow: hidden;
            }
            
            .ant-table-thead > tr > th,
            .table thead th {
                background-color: #F8FAFC !important;
                color: #1B2A3D !important;
                font-weight: 600 !important;
                border-bottom: 2px solid #E2E8F0 !important;
                text-transform: uppercase;
                font-size: 0.75rem;
                letter-spacing: 0.05em;
            }
            
            .ant-table-tbody > tr:hover,
            .table tbody tr:hover {
                background-color: #F8FAFC !important;
            }
            
            .ant-breadcrumb {
                font-size: 0.875rem;
            }
            
            .ant-breadcrumb-link {
                color: #64748B !important;
            }
            
            .ant-breadcrumb-link:hover {
                color: #0B7FC2 !important;
            }
            
            .ant-tag,
            .badge,
            .label {
                border-radius: 6px !important;
                font-weight: 500 !important;
                padding: 2px 8px !important;
            }
            
            .ant-tag-blue,
            .badge-primary {
                background-color: #E8F4FB !important;
                color: #0B7FC2 !important;
                border-color: #0B7FC2 !important;
            }
            
            .ant-tag-green,
            .badge-success {
                background-color: #ECFDF5 !important;
                color: #10B981 !important;
                border-color: #10B981 !important;
            }
            
            .ant-alert,
            .alert {
                border-radius: 8px !important;
                border-width: 1px !important;
            }
            
            .ant-alert-info,
            .alert-info {
                background-color: #E8F4FB !important;
                border-color: #0B7FC2 !important;
                color: #0A6BA0 !important;
            }
            
            .ant-alert-success,
            .alert-success {
                background-color: #ECFDF5 !important;
                border-color: #10B981 !important;
                color: #059669 !important;
            }
            
            .ant-tooltip-inner {
                background-color: #1B2A3D !important;
                border-radius: 6px !important;
                font-size: 0.875rem;
            }
            
            .ant-tooltip-arrow-content {
                background-color: #1B2A3D !important;
            }
            
            .ant-spin-dot-item {
                background-color: #0B7FC2 !important;
            }
            
            .ant-progress-bg {
                background-color: #0B7FC2 !important;
            }
            
            .ant-switch-checked {
                background-color: #10B981 !important;
            }
            
            .ant-checkbox-checked .ant-checkbox-inner,
            .ant-radio-checked .ant-radio-inner {
                background-color: #0B7FC2 !important;
                border-color: #0B7FC2 !important;
            }
            
            .ant-dropdown-menu,
            .dropdown-menu {
                border-radius: 8px !important;
                box-shadow: 0 4px 12px rgba(27, 42, 61, 0.1) !important;
                border: 1px solid #E2E8F0 !important;
            }
            
            .ant-dropdown-menu-item:hover,
            .dropdown-item:hover {
                background-color: #F8FAFC !important;
            }
            
            .grid-container,
            .dashboard-grid {
                background-color: #F5F8FA !important;
                padding: 16px !important;
            }
            
            ::-webkit-scrollbar {
                width: 8px;
                height: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background: #F1F5F9;
                border-radius: 4px;
            }
            
            ::-webkit-scrollbar-thumb {
                background: #CBD5E1;
                border-radius: 4px;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: #94A3B8;
            }
            
            .list-view,
            .table-view,
            .explorer {
                background-color: #FFFFFF !important;
                border-radius: 12px !important;
                border: 1px solid #E2E8F0 !important;
            }
            
            .filters-panel,
            .filter-container {
                background-color: #FFFFFF !important;
                border-radius: 8px !important;
                border: 1px solid #E2E8F0 !important;
                padding: 16px !important;
            }
            
            .SqlEditor,
            .ace_editor {
                border-radius: 8px !important;
                border: 1px solid #E2E8F0 !important;
            }
            
            .chart-controls,
            .control-panel {
                background-color: #FFFFFF !important;
                border-radius: 8px !important;
            }
        </style>
        """
        self.superset_app.config['CUSTOM_CSS'] = Markup(custom_css)

CUSTOM_SUPERSET_APP_INITIALIZER = CustomSupersetAppInitializer

ENABLE_TEMPLATE_PROCESSING = True

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_RBAC": True,
}

HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}

FAB_ADD_SECURITY_API = True
GUEST_TOKEN_JWT_SECRET = "da39a3ee5e6b4b0d3255bfef95601890afd80709"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_JWT_EXP_SECONDS = 3600

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['https://app.s4erp.com']
}

GUEST_ROLE_NAME = "Gamma"

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
