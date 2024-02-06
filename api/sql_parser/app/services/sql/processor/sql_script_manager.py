from abc import abstractmethod

from api.sql_parser.app.models import SqlProcessingMetadata


class SqlScriptManager:
    @abstractmethod
    def process(self, script_name: str) -> SqlProcessingMetadata:
        pass
