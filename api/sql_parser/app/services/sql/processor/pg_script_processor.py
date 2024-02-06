import os
from subprocess import CompletedProcess

from api.sql_parser.app.apps import Configuration
from api.sql_parser.app.models import SqlProcessingMetadata
from api.sql_parser.app.services.shell.shell_executor import ShellExecutor
from api.sql_parser.app.services.sql.accessor.sql_script_accessor import SqlScriptAccessor
from api.sql_parser.app.services.sql.processor.sql_script_processor import SqlScriptProcessor


class PostgresScriptProcessor(SqlScriptProcessor):
    shell_executor: ShellExecutor

    pg_port = 5432

    pg_matchers = ["pg", "postgres", "pg_dump"]

    db_uname = Configuration.db_user
    db_pwd = Configuration.db_password

    def __init__(self, shell_executor: ShellExecutor):
        super().__init__()
        self.shell_executor = shell_executor

    def supports_restore(self, script_heading: str) -> bool:
        script_heading = script_heading.casefold()

        for matcher in PostgresScriptProcessor.pg_matchers:
            if matcher.casefold() in script_heading:
                return True

        return False

    def form_db_name(self, for_script: str) -> str:
        return os.path.basename(for_script)

    def create_db(self, for_script: str) -> SqlProcessingMetadata:
        db_name = self.form_db_name(for_script)

        command = (f'PGPASSWORD={self.db_pwd} psql -U postgres -c "CREATE DATABASE {db_name} '
                   f'WITH OWNER = {self.db_uname} ENCODING = \'UTF8\';"')

        exec_res: CompletedProcess = (self.shell_executor
                                      .exec(command=command))

        return SqlProcessingMetadata(executor=self, command=command, exec_result=exec_res, db_name=db_name)

    def restore(self, script_path: str) -> SqlProcessingMetadata:
        db_name = self.form_db_name(script_path)

        command = (f'PGPASSWORD={self.db_pwd} pg_restore -U {self.db_uname} -d {db_name}'
                   f' -v {script_path}')

        exec_res: CompletedProcess = self.shell_executor.exec(command=command)

        return SqlProcessingMetadata(executor=self, command=command, exec_result=exec_res, db_name=db_name)

    def execute(self, script_path: str) -> SqlProcessingMetadata:
        db_name = self.form_db_name(script_path)

        command = (f'PGPASSWORD={self.db_pwd} psql -U {self.db_uname} -d {db_name} -f'
                   f' {script_path}')

        exec_res: CompletedProcess = self.shell_executor.exec(command=command)

        return SqlProcessingMetadata(executor=self, command=command, exec_result=exec_res, db_name=db_name)
