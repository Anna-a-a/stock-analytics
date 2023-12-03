import sqlite3

# Connect to SQLite database
con = sqlite3.connect("stock.db")

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




# Close the connection
con.close()
