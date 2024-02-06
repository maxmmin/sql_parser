from abc import abstractmethod
from subprocess import CompletedProcess



class ShellExecutor:
    """
    executes provided as arg command in the shell and returns it's result
    throws @Exception if command was failed
    """
    @abstractmethod
    def exec(self, command: str) -> CompletedProcess:
        pass
