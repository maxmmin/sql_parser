from environs import Env

env = Env()
env.read_env()


class AppConfig:
    db_user = env.str(name="SQL_USER")
    db_password = env.str(name="SQL_PWD")
    sql_scripts_path = env.str("SQL_SCRIPTS_PATH")
    pg_host = env.str("PGHOST")
