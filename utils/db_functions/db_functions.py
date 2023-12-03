import sqlite3


class DataBase:
    """
    Класс для работы с базой данных
    """

    def __init__(self, database_name: str):
        self.db_name = database_name
        self.con = sqlite3.connect(self.db_name, check_same_thread=False)


    def get_all_values_by_stock(self) -> list:
        cur = self.con.cursor()

        try:
            data = list(cur.execute(f'''SELECT name, ticker FROM stock''').fetchall())
            cur.close()
            return data
        finally:
            cur.close()


