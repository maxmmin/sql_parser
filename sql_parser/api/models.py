from docker.models.containers import ExecResult

from sql_parser.api.services.sql.processor.sql_script_processor import SqlScriptProcessor


class SqlProcessingMetadata:
    executor: SqlScriptProcessor
    command: str
    exec_result: ExecResult
    db_name: str

    def __init__(self, executor: SqlScriptProcessor, command: str, exec_result: ExecResult, db_name: str):
        self.executor = executor
        self.command = command
        self.exec_result = exec_result
        self.db_name = db_name
