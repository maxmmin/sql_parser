from abc import abstractmethod

from api.sql_parser.app.models import SqlProcessingMetadata


class SqlScriptProcessor:
    @abstractmethod
    def supports_restore(self, script_part: str) -> bool:
        pass

    @abstractmethod
    def restore(self, script_path: str) -> SqlProcessingMetadata:
        pass

    @abstractmethod
    def execute(self, script_path: str) -> SqlProcessingMetadata:
        pass
