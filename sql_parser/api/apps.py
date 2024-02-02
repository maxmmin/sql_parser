from django.apps import AppConfig


class Configuration(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api',
    sql_root_path = "/root/path",
    sql_engine_container_id = "container",
    emulated_db_user = "sql_parser_app",
    emulated_db_password = "238sdaj21"
    emulated_scripts_path = "/sql/scripts"


