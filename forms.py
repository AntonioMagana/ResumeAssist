from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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

class ResumeForm(FlaskForm):
    schoolName = StringField('School Name', validators=[DataRequired(), Length(min =3, max=40)])
    schoolDegree=StringField('School Degree', validators=[DataRequired(), Length(min =3, max=40)])
    schoolStartDate=StringField('Start Date', validators=[DataRequired(), Length(min =3, max=40)])
    schoolEndDate=StringField('End Date', validators=[DataRequired(), Length(min =3, max=40)])
    projectTitle = StringField('Project Title', validators=[DataRequired(), Length(min =3, max=40)])
    projectDescription = TextAreaField('Project Description', validators=[DataRequired(), Length(min =10, max=500)])
    projectTime = StringField('Time Frame', validators=[DataRequired(), Length(min =3, max=40)])
    workTitle = StringField('Work title', validators=[DataRequired(), Length(min =3, max=40)])
    workDescription = TextAreaField('Work Description', validators=[DataRequired(), Length(min =10, max=100)])
    workStartDate = StringField('Work Start Date', validators=[DataRequired(), Length(min =3, max=40)])
    workEndDate= StringField('Work End Date', validators=[DataRequired(), Length(min =3, max=40)])
    #submit = SubtmitField('Submit')
