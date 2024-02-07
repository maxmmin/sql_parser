import os
from subprocess import CompletedProcess
from typing import Optional

from app_config import AppConfig
from model.sql_processing_metadata import SqlProcessingMetadata
from service.shell.shell_executor import ShellExecutor
from service.sql.processor.sql_script_processor import SqlScriptProcessor


class PostgresScriptProcessor(SqlScriptProcessor):
    shell_executor: ShellExecutor

    pg_port = 5432

    pg_matchers = ["pg", "postgres", "pg_dump"]

    db_uname = AppConfig.db_user
    db_pwd = AppConfig.db_password

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
        return os.path.basename(for_script).split(".")[0]

    def create_db(self, db_name: str) -> SqlProcessingMetadata:
        command = (f'PGPASSWORD={self.db_pwd} psql -U {AppConfig.db_user} -h {AppConfig.pg_host} -c '
                   f'"CREATE DATABASE {db_name} '
                   f'WITH OWNER = {self.db_uname} ENCODING = \'UTF8\';"')

        exec_res: CompletedProcess = (self.shell_executor
                                      .exec(command=command))

        return SqlProcessingMetadata(executor=self, command=command, exec_result=exec_res, db_name=db_name)

    def safe_create_db(self, db_name: str) -> Optional[SqlProcessingMetadata]:
        try:
            return self.create_db(db_name)
        except Exception as e:
            print(f"Db creation err. Ignoring...\n{e}")
            return None

    def restore(self, script_path: str) -> SqlProcessingMetadata:
        db_name = self.form_db_name(script_path)

        self.safe_create_db(db_name)

        command = (f'PGPASSWORD={self.db_pwd} pg_restore -U {self.db_uname} -h {AppConfig.pg_host} -d {db_name}'
                   f' -v {script_path}')

        exec_res: CompletedProcess = self.shell_executor.exec(command=command)

        return SqlProcessingMetadata(executor=self, command=command, exec_result=exec_res, db_name=db_name)

    def execute(self, script_path: str) -> SqlProcessingMetadata:
        db_name = self.form_db_name(script_path)

        self.safe_create_db(db_name)

        command = (f'PGPASSWORD={self.db_pwd} psql -U {self.db_uname} -d {db_name} -f'
                   f' {script_path}')

        exec_res: CompletedProcess = self.shell_executor.exec(command=command)

        return SqlProcessingMetadata(executor=self, command=command, exec_result=exec_res, db_name=db_name)
