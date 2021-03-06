from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.registerform import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def fill_db():
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
    user1.position = "colonist"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "andrey_chief@mars.org"
    user1.hashed_password = "cap"
    session.add(user1)

    user2 = User()
    user2.surname = "Evgeniy"
    user2.name = "Ridley"
    user2.age = 19
    user2.position = "colonist"
    user2.speciality = "research engineer"
    user2.address = "module_1"
    user2.email = "evgeniy_chief@mars.org"
    user2.hashed_password = "cap"
    session.add(user2)

    user3 = User()
    user3.surname = "Lexa"
    user3.name = "Ridley"
    user3.age = 18
    user3.position = "colonist"
    user3.speciality = "research engineer"
    user3.address = "module_1"
    user3.email = "lexa_chief@mars.org"
    user3.hashed_password = "cap"
    session.add(user3)

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    session.add(job)

    job1 = Jobs()
    job1.team_leader = 1
    job1.job = 'b'
    job1.work_size = 20
    job1.collaborators = '1, 2'
    job1.is_finished = True
    session.add(job1)

    session.commit()


def main():
    db_session.global_init("db/blogs.db")
    #  fill_db()
    app.run()


if __name__ == '__main__':
    main()
