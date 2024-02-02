from abc import abstractmethod

from docker.models.containers import ExecResult


class DockerShellExecutor:
    """
    executes provided as arg command in the configured docker container and returns it's result
    throws @Exception if command was failed
    """
    @abstractmethod
    def exec(self, command: str) -> ExecResult:
        pass
