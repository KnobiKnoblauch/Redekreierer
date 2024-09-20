class DatabaseService:
    def __init__(self, database):
        self.cursor = database.getCursor()
        self.connection = database.getConnection()
        self.db = database

    def create_table(self, table_name, columns):
        print(f"Create table {table_name}")
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {columns}")
        print(f"Table {table_name} created successfully")

    def insert_prompt(self, speak_type):
        print("Erstelle Prompt-Types ...")
        prompts_to_insert = [
            (
                speak_type['topic'],
                speak_type['address'],
                speak_type['goal'],
                speak_type['speaker']
            ),
        ]
        self.cursor.executemany(
            "INSERT INTO prompt (topics, addresses, goals, speakers) VALUES (?, ?, ?, ?)",
            prompts_to_insert
        )
        self.db.saveChanges()
        print("Prompt-Types erstellt")

    def insert_score_points(self, score_type):
        print("Erstelle Punkteverteilung ...")
        self.cursor.executemany(
            "INSERT INTO score (quality, content, word_count) VALUES (?, ?, ?)",
            [
                (score_type["quality"], score_type["content"], score_type["length"]),
            ]
        )
        self.db.saveChanges()
        print("Punkteverteilung erstellt")

    def insert_improvement_points(self, improvement_score_type):
        print("Erstelle verbesserte Punkteverteilung ...")
        self.cursor.executemany(
            "INSERT INTO improvement (quality, content, word_count, how_much_more) VALUES (?, ?, ?, ? )",
            [
                (improvement_score_type["quality"], improvement_score_type["content"], improvement_score_type["length"],
                 improvement_score_type["differenz"]),
            ]
        )
        self.db.saveChanges()
        print("verbesserte Punkteverteilung erstellt")

    def select_table(self, table_name):
        # get last row of table
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", [id])
        return self.cursor.fetchone()

    def select_last_row_but_id(self, table_name, column):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if rows:
            last_row = rows[-1]
            print(last_row[column])
            return str(last_row[column])
        else:
            print("Die Tabelle ist leer.")
            return None

