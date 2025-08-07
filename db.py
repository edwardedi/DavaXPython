import sqlite3
from models import RequestModel


class Database:
    def __init__(self, db_path="requests.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT NOT NULL,
            input TEXT NOT NULL,
            output INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save_request(self, request: RequestModel):
        query = """
        INSERT INTO requests (operation, input, output, timestamp)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (request.operation,
                                  request.input,
                                  request.output,
                                  request.timestamp.isoformat()))
        self.conn.commit()
