import sqlite3

from utils.notify_admins import write_admin


class SQL:
    def __init__(self):
        """Initializing Database Connection"""
        self.conn = sqlite3.connect("karmaBD.db")
        self.cursor = self.conn.cursor()

    def checkDB(self):
        """проверяет наличие базы данных"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `karma_user` (
            userid INT NOT NULL,
            chatid INT NOT NULL,
            karma INT NULL DEFAULT 0,
            user_name TEXT,
            user_nick TEXT,
            is_banned TEXT NOT NULL DEFAULT False
            )""")
        self.conn.commit()
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS `accounts` (
        #     Id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     TelegramNikName TEXT,
        #     IDTelegram TEXT,
        #     Prava TEXT NOT NULL DEFAULT no,
        #     NumRentBike TEXT NOT NULL DEFAULT NO
        #     )""")
        # self.conn.commit()
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Bikes` (
        #     Id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     Model TEXT,
        #     RegNumber TEXT,
        #     Owner TEXT,
        #     OwnerPrise INT,
        #     OwnerDayPrice INT,
        #     OwnerRentStart TEXT,
        #     Profit INT NOT NULL DEFAULT 0,
        #     Status NOT NULL DEFAULT free,
        #     curentRentFinish TEXT
        #     )""")
        # self.conn.commit()

    def change_karma(self, todo, user_id):
        try:
            if todo == "plus":
                self.cursor.execute('''UPDATE karma_user SET karma = (karma + 1) WHERE userid = ?''',
                                    (user_id, ))
            elif todo == "minus":
                self.cursor.execute('''UPDATE karma_user SET karma = (karma - 1) WHERE userid = ?''',
                                    (user_id, ))
            self.cursor.execute('''SELECT karma FROM karma_user WHERE userid = ?''',
                                    (user_id, ))
            return self.cursor.fetchone()
        except sqlite3.Error as error:
            write_admin(f"Ошибка при работе с SQLite change_karma, {error}")
        finally:
            self.conn.commit()