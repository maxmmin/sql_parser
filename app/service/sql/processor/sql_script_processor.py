from abc import abstractmethod

from service.model.sql_processing_metadata import SqlProcessingMetadata


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


