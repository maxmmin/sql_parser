import subprocess
from subprocess import CompletedProcess


from api.sql_parser.app.services.shell.shell_executor import ShellExecutor
from api.sql_parser.app.util.check_out_exec_err import check_out_exec_err


class SimpleShellExecutor(ShellExecutor):
    def __init__(self):
        super().__init__()

    def exec(self, command: str) -> CompletedProcess:
        exec_result: CompletedProcess = subprocess.run(command, shell=True,
                                                       capture_output=True,
                                                       text=True)

        check_out_exec_err(exec_res=exec_result)

        return exec_result
