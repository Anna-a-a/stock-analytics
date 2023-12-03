import sqlite3


class DataBase:
    """
    Класс для работы с базой данных
    """

    def __init__(self, database_name: str):
        self.db_name = database_name
        self.con = sqlite3.connect(self.db_name, check_same_thread=False)

    def add_company(self, dict_of_value: dict) -> bool:
        """
        :param dict_of_value
        :return: None
        добавляет company в бд
        """
        list_of_value = list(dict_of_value.values())

        cur = self.con.cursor()
        request = f'''INSERT OR IGNORE INTO companies(company_name)
         VALUES({list_of_value[0]}");'''

        cur.execute(request)
        self.con.commit()
        cur.close()
        return 1

    def add_data(self, dict_of_value: dict) -> bool:
        """
        :param dict_of_value
        :return: None
        добавляет data в бд
        """
        list_of_value = list(dict_of_value.values())

        cur = self.con.cursor()
        request = f'''INSERT OR IGNORE INTO data(company_id, year, quarter, profit, debt)
         VALUES({list_of_value[0]}, {list_of_value[1]}, "{list_of_value[2]}", {list_of_value[3]},
          "{list_of_value[4]}"");'''

        cur.execute(request)
        self.con.commit()
        cur.close()
        return 1


    def get_all_values_by_company(self) -> list:
        cur = self.con.cursor()

        try:
            data = list(cur.execute(f'''SELECT year, quarter, profit, debt
FROM data
INNER JOIN companies ON companies.company_id = data.company_id;''').fetchall())
            cur.close()
            return data
        finally:
            cur.close()



"""
db = DataBase(f"{PROJECT_PATH}/static/db/database.db")

print(
    db.get_values_with_filter(
        'pk',
        type_pk='qw',
        class_pk='qw',
        details='qw',
        amount_of_RAM=123,
        CD_rom=True)
)
"""