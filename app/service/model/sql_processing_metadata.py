from subprocess import CompletedProcess


class SqlProcessingMetadata:
    executor: object
    command: str
    exec_result: CompletedProcess
    db_name: str

    def __init__(self, executor: object, command: str, exec_result: CompletedProcess, db_name: str):
        self.executor = executor
        self.command = command
        self.exec_result = exec_result
        self.db_name = db_name
