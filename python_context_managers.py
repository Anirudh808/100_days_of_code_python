import sqlite3
from contextlib import contextmanager

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'


# Class Based Custom Context Manager
class Database:

    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.Connection(self.path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"an error occurred: {exc_val}")
        self.connection.close()


# Generator Based Context Manager
@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'an error occurred: {e}')
    finally:
        connection.close()


def main():
    database_path = ':memory:'

    with database(database_path) as db:
        db.get('cursor').execute(create_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(insert_into_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(select_from_table_sql_statement)

        print(db.get('cursor').fetchall())


if __name__ == '__main__':
    main()
