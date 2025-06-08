import sqlite3
import os

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Menu:
    def __init__(self, db_path=None):
        if db_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(base_dir, "database", "menu.db")
        self.db_path = db_path
        self.items = self.load_items_from_db()

    def load_items_from_db(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT name, price FROM itens")
        rows = cursor.fetchall()

        items = [MenuItem(name, price) for name, price in rows]
        connection.close()
        return items
