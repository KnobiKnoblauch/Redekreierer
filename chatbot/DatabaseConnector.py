import sqlite3


class DatabaseConnector:
    __db = None
    __c = None

    def __init__(self):
        self.__db = sqlite3.connect('chatbot.sqlite', check_same_thread=False)
        self.__c = self.__db.cursor()

    def close(self):
        self.__db.commit()
        self.__db.close()

    def saveChanges(self):
        self.__db.commit()

    def getConnection(self):
        return self.__db

    def getCursor(self):
        return self.__c
