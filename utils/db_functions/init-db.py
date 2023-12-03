import sqlite3

# Connect to SQLite database
con = sqlite3.connect("utils/db_functions/stock.db")

# Create a cursor object
cur = con.cursor()

# Create a table
cur.execute("""CREATE TABLE stock (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    name   TEXT    NOT NULL,
    ticker   TEXT    NOT NULL
);
""")
cur.execute("""
CREATE TABLE dividends (
  stock_id    INTEGER NOT NULL,
  period_year INTEGER NOT NULL,
  amount_per_stock   NUMERIC(38, 2)  NOT NULL,
  FOREIGN KEY (stock_id)
     REFERENCES stock (stock_id)
);
""")

dividends = [(1, 2016, 0),
       (1, 2017, 8.11),
       (1, 2018, 13.47),
       (1, 2019, 11.14),
       (1, 2020, 13.62),
       (1, 2021, 15.17),
       (1, 2022, 21.67),
       (1, 2023, 18.83)]

# Insert data into table
cur.execute("INSERT INTO stock(name, ticker) VALUES ('Ленэнерого П', 'LSNGP')")
cur.executemany('INSERT INTO dividends VALUES (?,?,?);', dividends)



# Close the connection
con.commit()
con.close()
