import sqlite3


# класс для работы с базой данных
class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect('songs_db.db')
        self.cursor = self.connection.cursor()

    # функция для получения всех данных из таблицы
    def tab_conclusion(self, list_name):
        self.cursor.execute(f"""SELECT title FROM '{list_name}'""")
        tab_data = self.cursor.fetchall()
        self.connection.close()
        return tab_data

    # функция для добавления нового файла в таблицу
    def add_files(self, list_name, file):
        self.cursor.execute(f"""INSERT INTO '{list_name}' VALUES (?)""", (file,))
        self.connection.commit()
        self.connection.close()

    # функция для удаления выбранного файла из таблицы
    def delete_one_file(self, list_name, file):
        self.cursor.execute(f"""DELETE FROM '{list_name}'
                            WHERE title = (?)""", (file,))
        self.connection.commit()
        self.connection.close()

    # функция для удаления всех файлов из таблицы
    def delete_all_files(self, list_name):
        self.cursor.execute(f"""DELETE FROM '{list_name}'""")
        self.connection.commit()
        self.connection.close()

    # функция для создания таблицы
    def create_table(self, tab_name):
        self.cursor.execute(f"""CREATE TABLE '{tab_name}' (title TEXT)""")
        self.connection.commit()
        self.connection.close()

    # функция для удаления таблицы
    def delete_tabel(self, tab_name):
        self.cursor.execute(f"""DROP TABLE '{tab_name}'""")
        self.connection.commit()
        self.connection.close()
