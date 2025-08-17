import os
import mysql.connector

class DataLoader:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "mysql")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "appuser")
        self.password = os.getenv("DB_PASSWORD", "apppass")
        self.database = os.getenv("DB_NAME", "appdb")

    def startup(self):
        cnx = mysql.connector.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, database=self.database
        )
        try:
            cur = cnx.cursor(dictionary=True)
            cur.execute("CREATE TABLE data (ID int NOT NULL,first_name varchar(255),last_name varchar(255),PRIMARY KEY (ID))")
            cur.execute("INSERT INTO data (first_name, last_name) VALUES ('Ada','Lovelace'),('Alan','Turing'),('Grace','Hopper'),('Edsger','Dijkstra'),('Barbara','Liskov');")
        finally:
            cur.close()
            cnx.close()

    def fetch_all(self):
        cnx = mysql.connector.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, database=self.database
        )
        try:
            cur = cnx.cursor(dictionary=True)
            cur.execute("SELECT id, first_name, last_name FROM data")
            return cur.fetchall()
        finally:
            cur.close()
            cnx.close()
