from flask import Flask, render_template, request
from forms.register import RegisterForm
from models import db, User
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key ='5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221269e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def index():


    return render_template('base.html')
    

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
# Обработка данных из формы
        firstnameUserUser = form.firstname.data
        lastnameUser = form.lastname.data
        emailUser = form.email.data
        passwordUser = form.password.data
        #print(firstname, lastname, email, password)

        user = User(firstname=firstnameUserUser, lastname=lastnameUser, email=emailUser)
        user.set_pass(passwordUser)
        db.session.add(user)
        db.session.commit()
        

    return render_template('form.html', form=form)

@app.route('/users/')
def get_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)