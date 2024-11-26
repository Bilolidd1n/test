from database import DatabaseManager
from roli import User, Admin, Customer

db = DatabaseManager()

user1 = User(name="Isko", email="isko1@gmail.com", age=20)
user1.add_user(db)
user2 = User(name="Sodiq", email="muhammadsodiq@gmail.com", age=20)
user2.add_user(db)
user3 = User(name="Biloliddin", email="Biloliddin@gmail.com", age=20)
user3.add_user(db)

admin1 = Admin(name="Bilol", email="bilol@gmail.com", age=25)
admin1.add_admin(db)
admin2 = Admin(name="mirza", email="olimjon@gmail.com", age=25)
admin2.add_admin(db)
admin3 = Admin(name="sodiqkot", email="kotsodiq@gmail.com", age=25)
admin3.add_admin(db)

customer1 = Customer(name="sariq", email="jeltiy@gmail.com", age=30)
customer1.add_customer(db)
customer2 = Customer(name="hello", email="niger@gmail.com", age=30)
customer2.add_customer(db)
customer3 = Customer(name="sariqbola", email="pizza@gmail.com", age=30)
customer3.add_customer(db)

user_to_find = User(name="", email="", age=0)
found_user = user_to_find.find_user_by_email(db, "isko1@gmail.com")
if found_user:
    print(f"Найден пользователь: {found_user.name}, {found_user.email}, {found_user.age}")

user_to_delete = User(name="", email="", age=0)
user_to_delete.delete_user(db, "isko1@gmail.com")
print("Пользователь удалён.")

db.close()
