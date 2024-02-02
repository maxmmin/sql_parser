from typing import List

from sql_parser.api.apps import Configuration
from sql_parser.api.services.shell.docker_shell_executor import DockerShellExecutor
from sql_parser.api.services.shell.simple_docker_shell_executor import SimpleDockerShellExecutor
from sql_parser.api.services.sql.sqlexec.sql_script_executor import SqlScriptExecutor

docker_executor: DockerShellExecutor = SimpleDockerShellExecutor(Configuration.sql_engine_container_id)

sql_executors: List[SqlScriptExecutor] = []
