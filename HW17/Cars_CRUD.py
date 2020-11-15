import sqlite3


class BrandsCRUD:

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
        create_table_query = """CREATE TABLE IF NOT EXISTS brands(
                            name1 VARCHAR
                    )
        """
        self.cursor.execute(create_table_query)

    def read_table(self):
        self.cursor.execute('''SELECT * FROM brands''')
        for row in self.cursor.fetchall():
            print(row)

    def create_brand(self, name1: str):
        create_brand_query = f'INSERT INTO brands(name1) VALUES (?)'
        self.cursor.execute(create_brand_query, (name1,))
        self.connection.commit()
        print(f'Brand {name1} was successfully created!')

    def delete_brand(self, name1: str):
        delete_brand_query = f'DELETE FROM brands WHERE name1 = ?'
        self.cursor.execute(delete_brand_query, (name1,))
        self.connection.commit()

    def update_brand(self, name1: str):
        update_brand_query = f'UPDATE brands SET name1 = "Renault" WHERE name1 = ?'
        self.cursor.execute(update_brand_query, (name1,))
        self.connection.commit()


class CarsCRUD:

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
        create_table_query = """CREATE TABLE IF NOT EXISTS cars(
                            car_id integer PRIMARY KEY AUTOINCREMENT,
                            brand integer,
                            model VARCHAR,
                            release_year INTEGER,
                            FOREIGN KEY (brand) 
                                REFERENCES brands (name1) 
                                    ON DELETE CASCADE
                    )
        """
        self.cursor.execute(create_table_query)

    def read_table(self):
        self.cursor.execute('''SELECT * FROM cars''')
        for row in self.cursor.fetchall():
            print(row)

    def create_car(self, brand: str, model: str, release_year: int) -> int:
        create_car_query = f'INSERT INTO cars(brand, model, release_year) VALUES (?, ?, ?)'
        self.cursor.execute(create_car_query, (brand, model, release_year))
        self.connection.commit()
        print(f'Car {model}, {release_year} was successfully created!')

    def delete_car(self, model: str):
        delete_car_query = f'DELETE FROM cars WHERE model = ?'
        self.cursor.execute(delete_car_query, (model,))
        self.connection.commit()

    def update_car(self, model: str):
        delete_car_query = f'UPDATE cars SET model = "Passat" WHERE model = ?'
        self.cursor.execute(delete_car_query, (model,))
        self.connection.commit()


if __name__ == '__main__':

    table1 = CarsCRUD(db_name='cars1.db')
    table2 = BrandsCRUD(db_name='brands1.db')
    table2.create_table()
    table1.create_table()
    table1.connection.close()
    table1.cursor.close()
    table2.connection.close()
    table2.cursor.close()
