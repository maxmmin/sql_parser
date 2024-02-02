import docker
from docker.models.containers import ExecResult, Container

from sql_parser.api.services.shell.docker_shell_executor import DockerShellExecutor
from docker.client import DockerClient

from sql_parser.api.util.check_out_exec_err import check_out_exec_err


class SimpleDockerShellExecutor(DockerShellExecutor):
    docker_client: DockerClient = docker.from_env()

    def __init__(self, sql_engine_container_id: str):
        super().__init__()
        self.sql_engine_container_id = sql_engine_container_id

    def exec(self, command: str) -> ExecResult:
        container: Container = self.docker_client.containers.get(self.sql_engine_container_id)

        exec_result: ExecResult = container.exec_run(cmd=command, stdout=True,
                                                     stderr=True,
                                                     tty=True)

        check_out_exec_err(exec_res=exec_result)

        return exec_result
