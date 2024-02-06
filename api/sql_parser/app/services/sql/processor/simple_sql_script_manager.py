from typing import List, Optional

from api.sql_parser.app.apps import Configuration
from api.sql_parser.app.models import SqlProcessingMetadata
from api.sql_parser.app.services.sql.accessor.fs_sql_script_accessor import FileSystemSqlScriptAccessor
from api.sql_parser.app.services.sql.accessor.sql_script_accessor import SqlScriptAccessor
from api.sql_parser.app.services.sql.processor.pg_script_processor import PostgresScriptProcessor
from api.sql_parser.app.services.sql.processor.sql_script_manager import SqlScriptManager
from api.sql_parser.app.services.sql.processor.sql_script_processor import SqlScriptProcessor


class SimpleSqlScriptManager(SqlScriptManager):
    sql_script_accessor: SqlScriptAccessor
    sql_processors: List[SqlScriptProcessor]

    def __init__(self, sql_script_accessor: SqlScriptAccessor, sql_processors: List[SqlScriptProcessor]):
        super().__init__()
        self.sql_script_accessor = sql_script_accessor
        self.sql_processors = sql_processors

    def process(self, script_name: str) -> Optional[SqlProcessingMetadata]:
        print(f"Running {script_name} recovery")

        script_heading = self.get_script_heading(script_name)
        script_path = self.sql_script_accessor.build_script_path(script_name)

        metadata: Optional[SqlProcessingMetadata] = None

        for processor in self.sql_processors:
            if metadata:
                break

            pr_name = processor.__class__.__name__

            print(f"Checking restoration support for {script_name} with: {pr_name}...")

            if processor.supports_restore(script_heading):
                try:
                    print(f"Trying to restore with {pr_name}")
                    metadata = processor.restore(script_path)
                except Exception as e:
                    print(f"Processor {pr_name} failed at restoring with next error: {e}")
            else:
                print(f"{pr_name}: restoration is not supported")

        if not metadata:
            print("Native restoration is not supported. Trying force sql executing...")
            for processor in self.sql_processors:
                if metadata:
                    break
                pr_name = processor.__class__.__name__

                try:
                    print(f"Trying force sql executing with {pr_name}")
                    metadata = processor.execute(script_path)
                except Exception as e:
                    print(f"Processor {pr_name} failed at sql executing with next error: {e}")

        if metadata:
            print(f"Script {script_name} was successfully recovered\n{metadata}")
        else:
            print(f"Script {script_name} wasn't recovered.")

        return metadata

    def get_script_heading(self, script_name: str):
        return self.sql_script_accessor.get(script_name=script_name, lines_amount=100)


test_manager = SimpleSqlScriptManager(sql_script_accessor=FileSystemSqlScriptAccessor(Configuration.sql_root_path), sql_processors=[PostgresScriptProcessor()])