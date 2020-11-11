import sqlite3


class PersonCRUD:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = self.__get_connection()
        self.cursor = self.__get_cursor()

    def __get_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(str(e))
            return

    def __get_cursor(self):
        return self.connection.cursor()

    def create_table(self):
        create_table_query = """CREATE TABLE IF NOT EXISTS person(
                            person_id integer PRIMARY KEY AUTOINCREMENT,
                            first_name VARCHAR,
                            last_name VARCHAR,
                            age INTEGER
                    )
        """
        self.cursor.execute(create_table_query)

    def read_table(self):
        self.cursor.execute('''SELECT * FROM person''')
        for row in self.cursor.fetchall():
            print(row)

    def create_person(self, first_name: str, last_name: str, age: int) -> int:
        create_person_query = f'INSERT INTO person(first_name, last_name, age) VALUES (?, ?, ?)'
        self.cursor.execute(create_person_query, (first_name, last_name, age))
        self.connection.commit()
        print(f'Person {first_name} {last_name} {age} was successfully created!')

    def delete_person(self, first_name: str):
        delete_person_query = f'DELETE FROM person WHERE first_name = ?'
        self.cursor.execute(delete_person_query, (first_name,))
        self.connection.commit()

    def update_person(self, age: int):
        delete_person_query = f'UPDATE person SET age = 20 WHERE age = ?'
        self.cursor.execute(delete_person_query, (age,))
        self.connection.commit()

    def get_persons_with_my_name(self, my_name: str):
        my_name_query = f'SELECT last_name FROM person WHERE first_name = ?'
        self.cursor.execute(my_name_query, (my_name,))
        for row in self.cursor.fetchall():
            print(row)
        self.connection.commit()

    def younger_than_25(self, appropriate_age: int):
        my_name_query = f'SELECT first_name, last_name, age FROM person WHERE age < ?'
        self.cursor.execute(my_name_query, (appropriate_age,))
        for row in self.cursor.fetchall():
            print(row)
        self.connection.commit()

    def from_15_to_18(self, bottom_border, upper_border: int):
        my_name_query = f'SELECT first_name, last_name, age FROM person WHERE age BETWEEN ? AND ?'
        self.cursor.execute(my_name_query, (bottom_border, upper_border,))
        for row in self.cursor.fetchall():
            print(row)
        self.connection.commit()


if __name__ == '__main__':

    table = PersonCRUD(db_name='database1.db')
    table.create_table()
    table.get_persons_with_my_name('Andrey')
    print('________________')
    table.younger_than_25(25)
    print('________________')
    table.from_15_to_18(15, 18)
    table.delete_person('Anton')
    table.update_person(19)


