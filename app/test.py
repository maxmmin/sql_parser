import time

from app_config import AppConfig
from service.shell.simple_shell_executor import SimpleShellExecutor
from service.sql.accessor.fs_sql_script_accessor import FileSystemSqlScriptAccessor
from service.sql.processor.pg_script_processor import PostgresScriptProcessor
from service.sql.simple_sql_script_manager import SimpleSqlScriptManager

processors = [PostgresScriptProcessor(SimpleShellExecutor())]

time.sleep(5)

sql_script_manager = SimpleSqlScriptManager(sql_processors=processors,
                                            sql_script_accessor=FileSystemSqlScriptAccessor(AppConfig.sql_scripts_path))

data = sql_script_manager.process("backup_file.sql")

if data:
    print(f"Recovery finished: {data.db_name}"
          f"\nShell exit code: {data.exec_result.returncode}"
          f"\nOutput: {data.exec_result.stdout}"
          f"\nError output: {data.exec_result.stderr}")
else:
    print("Err. Exiting...")


