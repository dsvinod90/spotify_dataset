import sys
import psycopg2


class DatabaseInitializer:
    def __init__(self, hostname: str, dbname: str) -> None:
        self.connection = psycopg2.connect(host=hostname, dbname=dbname)
        self.connection.set_session(autocommit=True)
        self.cursor = self.connection.cursor()
        
    def _execute_ddl_queries(self, script_path: str) -> None:
        self.cursor.execute(open(script_path, 'r').read())

    def execute(self):
        self._execute_ddl_queries('sql_scripts/create_schema.sql', )
        self._execute_ddl_queries('sql_scripts/populate_temp_table.sql')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        hostname = sys.argv[1]
        dbname = sys.argv[2]
        db_init = DatabaseInitializer(hostname, dbname)
        db_init.execute()