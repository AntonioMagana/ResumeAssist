import flask_login
from flask import Flask, render_template, url_for, flash, redirect, request, send_file
from flask_login import current_user, login_required, login_user, logout_user
from flask_login import LoginManager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from io import BytesIO

from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '57916289bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
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
    name = db.Column(db.String(200))
    resume = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<post: {self.text}>'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


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
        return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if form.password.data == user.password:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
        flash('Incorrect username/password. Try again.')
    return render_template('login.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/selection')
def selection():
    return render_template('selection.html')


@app.route('/save', methods=['POST'])
def save():
    file = request.files['inputFile']
    newFile = ResumeList(name=file.name, resume=file.read())
    db.session.add(newFile)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    file_data = ResumeList.query.filter_by(id=1).first()
    return send_file(BytesIO(file_data.resume), attachment_filename='flask.pdf', as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
