import sys

from converter import Converter
from database_initializer import DatabaseInitializer


class Main:
    def execute(self):
        input_data_folder = None
        hostname = None
        database_name = None
        username = None
        password = None
        if len(sys.argv) < 4:
            print('Invalid input')
            sys.exit(1)
        if len(sys.argv) >= 4:
            input_data_folder = sys.argv[1]
            hostname = sys.argv[2]
            database_name = sys.argv[3]
        if len(sys.argv) >= 5:
            username = sys.argv[4]
        if len(sys.argv) == 6:
            password = sys.argv[5]
        Converter().execute(input_data_folder)
        DatabaseInitializer(hostname, database_name, username, password).execute()
        sys.exit(0)


if __name__ == '__main__':
    Main().execute()