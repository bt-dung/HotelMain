import mysql.connector
from mysql.connector import Error

class DatabaseHandler:
    def __init__(self, host, user, database):
        self.host = host
        self.user = user
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host, user=self.user, database=self.database)
            return self.connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_all(self, query, params=None):
        """Lấy tất cả kết quả từ truy vấn."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def fetch_one(self, query, params=None):
        """Lấy một kết quả duy nhất từ truy vấn."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def close(self):
        """Đóng kết nối đến cơ sở dữ liệu."""
        if self.connection:
            self.connection.close()