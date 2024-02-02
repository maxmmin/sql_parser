import os.path
from abc import abstractmethod
from typing import Optional


class SqlScriptAccessor:

    @abstractmethod
    def exists(self, script_name: str) -> bool:
        pass

    @abstractmethod
    def get(self, script_name: str, lines_amount: Optional[int]) -> str:
        pass

