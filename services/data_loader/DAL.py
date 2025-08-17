import os
import mysql.connector

class DataLoader:
    def __init__(self):
        # self.host = os.getenv("MYSQL_URL", "mysql")
        # self.port = int(os.getenv("DB_PORT", "3306"))
        # self.user = os.getenv("DB_USER", "user")
        # self.password = os.getenv("DB_PASSWORD", "password")
        # self.database = os.getenv("DB_NAME", "mydb")

        self.host = "mysql"
        # self.port = 3306
        self.user = "user"
        self.password = "password"
        self.database = "mydb"

    def startup(self):
        cnx = mysql.connector.connect(
            host=self.host, port=self.port, user=self.user,
            password=self.password, database=self.database
        )
        try:
            cur = cnx.cursor(dictionary=True)
            cur.execute("CREATE TABLE IF NOT EXISTS data (ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,first_name varchar(255),last_name varchar(255));")
            cur.execute("INSERT INTO data (first_name, last_name) VALUES ('Ada','Lovelace'),('Alan','Turing'),('Grace','Hopper'),('Edsger','Dijkstra'),('Barbara','Liskov')")
        finally:
            cur.close()
            cnx.commit()
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
