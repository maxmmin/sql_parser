from abc import abstractmethod

from model.sql_processing_metadata import SqlProcessingMetadata


class SqlScriptManager:
    @abstractmethod
    def process(self, script_name: str) -> SqlProcessingMetadata:
        pass
