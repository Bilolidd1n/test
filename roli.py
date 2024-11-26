from database import DatabaseManager

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def add_user(self, db):
        query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
        db.cursor.execute(query, (self.name, self.email, self.age))
        db.connection.commit()

    def find_user_by_email(self, db, email):
        query = "SELECT * FROM users WHERE email = ?"
        db.cursor.execute(query, (email,))
        user_data = db.cursor.fetchone()
        if user_data:
            return User(name=user_data[1], email=user_data[2], age=user_data[3])
        return None

    def delete_user(self, db, email):
        query = "DELETE FROM users WHERE email = ?"
        db.cursor.execute(query, (email,))
        db.connection.commit()


class Admin(User):
    def add_admin(self, db):
        query = "INSERT INTO admin_users (name, email, age) VALUES (?, ?, ?)"
        db.cursor.execute(query, (self.name, self.email, self.age))
        db.connection.commit()


class Customer(User):
    def add_customer(self, db):
        query = "INSERT INTO customer_users (name, email, age) VALUES (?, ?, ?)"
        db.cursor.execute(query, (self.name, self.email, self.age))
        db.connection.commit()
