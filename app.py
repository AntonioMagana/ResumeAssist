from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_login import LoginManager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, ResumeForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '57916289bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bootstrap = Bootstrap(app)

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(60))
    resumeList = db.relationship('ResumeList', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<user: {self.username}>'

class ResumeList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(200))
    work = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<post: {self.text}>'

posts = [
    {
        'author': 'Sair',
        'title': 'Resume One',
        'content': 'random info',
        'date_posted': 'April 1st'
    },
    {
        'author': 'Anthony',
        'title': 'Resume Two',
        'content': 'random info',
        'date_posted': 'April 2nd'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

#did not do database stuff yet
@app.route("/questions", methods=['GET','POST'])
def questions():
    form = ResumeForm()
    #if form.validate_on_submit():
        #db.session.add()
        #db.session.commit()
        #flash('You submitted data for your resume')
        #return redirect(url_for('home')) #probably just redirect to the next questionnaire page like work exp
    return render_template('QTest2.html',title='Resume Questions',form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = form.password.data
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))
        flash('Incorrect username/password. Try again.')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
