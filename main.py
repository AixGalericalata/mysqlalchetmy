from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)

    user1 = User()
    user1.surname = "Andrey"
    user1.name = "Ridley"
    user1.age = 20
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "andrey_chief@mars.org"
    user1.hashed_password = "cap"
    session.add(user1)

    user2 = User()
    user2.surname = "Evgeniy"
    user2.name = "Ridley"
    user2.age = 19
    user2.position = "captain"
    user2.speciality = "research engineer"
    user2.address = "module_1"
    user2.email = "evgeniy_chief@mars.org"
    user2.hashed_password = "cap"
    session.add(user2)

    user3 = User()
    user3.surname = "Lexa"
    user3.name = "Ridley"
    user3.age = 18
    user3.position = "captain"
    user3.speciality = "research engineer"
    user3.address = "module_1"
    user3.email = "lexa_chief@mars.org"
    user3.hashed_password = "cap"
    session.add(user3)

    session.commit()
    #  app.run()


if __name__ == '__main__':
    main()
