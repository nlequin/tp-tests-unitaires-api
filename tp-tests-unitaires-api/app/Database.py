import sqlite3

class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect(':memory:', check_same_thread=False)
        self.conn.row_factory = self.dict_factory
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, age INTEGER)")

    def dict_factory(self, cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    def create(self, user):
        self.cursor.execute("INSERT INTO users(name, age) VALUES (?,?)", (user.name, user.age))
        return self.cursor.rowcount == 1

    def read(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id =?",(id,))
        rows = self.cursor.fetchone()
        if(rows != None):
            return rows
        else :
            return ""

    def read_all(self):
        self.cursor.execute("SELECT id, name, age FROM users")
        rows = self.cursor.fetchall()
        return rows
    
    def update(self, user):
        self.cursor.execute("UPDATE users SET name =?, age =? WHERE id =?",(user.name, user.age, user.id))
        return self.cursor.rowcount >= 1
    
    def delete(self, id):
        self.cursor.execute("DELETE FROM users WHERE id =?",(id,))
        return self.cursor.rowcount >= 1