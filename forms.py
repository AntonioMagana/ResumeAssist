from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Rememeber Me')
    submit   = SubmitField('Sign In')

class SchoolForm(FlaskForm):
    schoolName = StringField('School Name', validators=[DataRequired(), Length(min =3, max=40)])
    schoolDegree=StringField('School Degree', validators=[DataRequired(), Length(min =3, max=40)])
    schoolStartDate=StringField('Start Date', validators=[DataRequired(), Length(min =3, max=40)])
    schoolEndDate=StringField('End Date', validators=[DataRequired(), Length(min =3, max=40)])
    #submit = SubtmitField('Submit')
