import sqlite3

# Connect to SQLite database
con = sqlite3.connect("db/stock.db")

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

cur.execute("""
CREATE TABLE report_data (
  stock_id    INTEGER NOT NULL,
  year INTEGER NOT NULL,
  q INTEGER NOT NULL,
  revenue   NUMERIC(38, 2)  NOT NULL,
  net_income NUMERIC(38, 2)  NOT NULL,
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

cur.execute("INSERT INTO stock(name, ticker) VALUES ('L p', 'LSNGP')")
cur.executemany('INSERT INTO dividends VALUES (?,?,?);', dividends)

report_data = [(1, 2019, 1, 21.1, 4.3),
       (1, 2019, 2, 18.7, 3.5),
       (1, 2019, 3, 18.7, 2.2),
       (1, 2019, 4, 23.9, 3.6),

       (1, 2020, 1, 21.6, 4.3),
       (1, 2020, 2, 17.8, 3.3),
       (1, 2020, 3, 19.4, 4.2),
       (1, 2020, 4, 23.8, 2.3),

       (1, 2021, 1, 24.0, 5.6),
       (1, 2021, 2, 22.5, 5.7),
       (1, 2021, 3, 21.2, 4.9),
       (1, 2021, 4, 25.7, 3.6),

       (1, 2022, 1, 24.8, 5.5),
       (1, 2022, 2, 21.3, 4.8),
       (1, 2022, 3, 21.8, 4.4),
       (1, 2022, 4, 27.2, 3.3),

       (1, 2023, 1, 25.3, 7.9),
       (1, 2023, 2, 28.3, 6.1),
       (1, 2023, 3, 24.1, 5.0)]
cur.executemany('INSERT INTO report_data VALUES (?,?,?,?,?);', report_data)

# Close the connection
con.commit()
con.close()
