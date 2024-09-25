

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

    def insert_speech(self, speech, name):
        print("Speichere speech")
        self.cursor.execute("INSERT INTO saved_speeches (speech, name) VALUES (?, ?)",
                            [
                                speech, name
                            ])
        self.db.saveChanges()
        print("speech gespeichert")

    def select_table(self, table_name, column_name):

        self.cursor.execute(f"SELECT {column_name} FROM {table_name}")

        rows = self.cursor.fetchall()

        return [row[0] for row in rows]

    def select_table_spalte(self, table_name, column_name, id):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id=?", (id,))
        result = self.cursor.fetchone()  # Holt nur eine Zeile

        if result:
            return result[0]  # Gibt den tatsächlichen Wert ohne Tupel oder Liste zurück
        else:
            return None  # Falls kein Ergebnis gefunden wurde

    def select_table_id(self, table_name, column_name, name):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE name=?", [name])
        result = self.cursor.fetchall()

        return result[0]

    def select_table_name(self, table_name, column_name, id):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id=?", (id,))
        result = self.cursor.fetchone()  # Holt nur eine Zeile

        if result:
            return result[0]
        else:
            return None

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

    def select_speech_type_params(self, table_name):
        query = f"SELECT topics, addresses, goals, speakers FROM {table_name}"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        if rows:
            last_row = rows[-1]
            return {
                "topic": last_row[0],
                "adresse": last_row[1],
                "goal": last_row[2],
                "speaker": last_row[3]
            }

        else:
            print("Die Tabelle ist leer.")
            return None

    def delete_speech(self, id):
        self.cursor.execute("DELETE FROM saved_speeches WHERE id = ?", (id,))
        self.db.saveChanges()
