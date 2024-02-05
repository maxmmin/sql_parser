import os

from django.apps import AppConfig


class Configuration(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app',
    sql_root_path = os.getenv("SQL_ROOT_PATH"),
    pg_host = os.getenv("PG_HOST"),
    db_user = "sql_parser_app",
    db_password = "238sdaj21"
    scripts_path = "/sql/scripts"
