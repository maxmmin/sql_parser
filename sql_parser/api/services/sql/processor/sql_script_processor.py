from abc import abstractmethod

from sql_parser.api.models import SqlProcessingMetadata


class SqlScriptProcessor:
    @abstractmethod
    def supports_restore(self, script_name: str) -> bool:
        pass

    @abstractmethod
    def restore(self, script_name: str) -> SqlProcessingMetadata:
        pass

    @abstractmethod
    def execute(self, script_name: str) -> SqlProcessingMetadata:
        pass
