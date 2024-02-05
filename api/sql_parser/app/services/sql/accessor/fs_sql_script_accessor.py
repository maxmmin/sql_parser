import os
from typing import Optional

from api.sql_parser.app.services.sql.accessor.sql_script_accessor import SqlScriptAccessor


class FileSystemSqlScriptAccessor(SqlScriptAccessor):
    sql_scripts_root: str

    def __init__(self, sql_scripts_root: str):
        super().__init__()
        self.sql_scripts_root = sql_scripts_root

    def build_script_path(self, script_name):
        script_path = os.path.abspath(os.path.join(self.sql_scripts_root, script_name))
        if script_path.startswith(self.sql_scripts_root):
            return script_path
        else:
            raise Exception(f"disallowed script location: {script_path}")

    def exists(self, script_name: str):
        script_path = self.build_script_path(script_name)
        return os.path.exists(script_path)

    def get(self, script_name: str, lines_amount: Optional[int]) -> str:
        script_path = self.build_script_path(script_name)

        with open(script_path, 'r') as file:
            if lines_amount is None:
                return file.read()
            else:
                return "\n".join(file.readlines(lines_amount))
