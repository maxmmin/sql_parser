import time

from app_config import AppConfig
from service.shell.simple_shell_executor import SimpleShellExecutor
from service.sql.accessor.fs_sql_script_accessor import FileSystemSqlScriptAccessor
from service.sql.processor.pg_script_processor import PostgresScriptProcessor
from service.sql.simple_sql_script_manager import SimpleSqlScriptManager

processors = [PostgresScriptProcessor(SimpleShellExecutor())]

sql_script_manager = SimpleSqlScriptManager(sql_processors=processors,
                                            sql_script_accessor=FileSystemSqlScriptAccessor(AppConfig.sql_scripts_path))

time.sleep(5)

data = sql_script_manager.process("backup_file.sql")

if data:
    print(f"Recovery finished: {data.db_name}"
          f"Output: {data.exec_result.stdout}")
else:
    print("Err. Exiting...")


