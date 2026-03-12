import sqlite3
import pandas as pd

class FoodStorage:
    def __init__(self, db_name="food_data.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """Membuat skema tabel restoran jika belum ada."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rating REAL,
                    link TEXT,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def save_restaurants(self, df: pd.DataFrame):
        """Menyimpan data dari Pandas DataFrame ke SQLite."""
        if df.empty:
            print("No data to save.")
            return

        with sqlite3.connect(self.db_name) as conn:
            df.to_sql('restaurants', conn, if_exists='append', index=False)
            print(f"Successfully saved {len(df)} records to {self.db_name}")