import sqlite3

# Connect to SQLite database
con = sqlite3.connect("tutorial1.db")

# Create a cursor object
cur = con.cursor()

# Create a table
cur.execute("""CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    company_name   TEXT    NOT NULL
);
""")
cur.execute("""CREATE TABLE data (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    year   TEXT    NOT NULL,
    quarter     TEXT    NOT NULL,
    profit       FLOAT,
    debt   FLOAT
);
""")


# Close the connection
con.close()
