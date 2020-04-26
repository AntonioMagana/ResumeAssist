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
    submit = SubmitField('Sign In')


# NEEDS TO BE CHANGED LATER. JUST A BASE TO WORK FROM
""" class Questionnaire(FlaskForm):
    personal_info = {
        name = StringField('Full Name', validators=[DataRequired()])
        phoneNumber = StringField('Phone Number', validator=s[DataRequired()])
        website = StringField('Your Portfolio Website')
    }
    education = {
        school = StringField('University/School name', validators=[DataRequired()])
        degree = StringField('Major or Degree if applicable')
        startDate = StringField('Month and year you started', validators=[DataRequired()])
        endDate = StringField('Month and year you ended or expected end date', validators=[DataRequired()])
        gpa = StringField('Your GPA')
        coursework = StringField('Your relevant coursework')
    }
    experience = {
        experience1 = {
            name = StringField('Your employer', validators=[DataRequired()])
            place = StringField('Where you worked', validators=[DataRequired()])
            startDate = StringField('Month and year you started', validators=[DataRequired()])
            endDate = StringField('Month and you ended. If still working, write Present', validators=[DataRequired()])
            position = StringField('What you worked as', validators=[DataRequired()])
            bullet1 = StringField('One sentence about your duties', validators=[DataRequired(), Length(min=20, max=150)])
            bullet2 = StringField('One sentence about your duties', validators=[DataRequired(), Length(min=20, max=150)])
            bullet3 = StringField('One sentence about your duties', validators=[DataRequired(), Length(min=20, max=150)])
        }
        experience2 = {
            name = StringField('Your employer')
            place = StringField('Where you worked')
            startDate = StringField('Month and year you started')
            endDate = StringField('Month and you ended. If still working, write Present')
            position = StringField('What you worked as')
            bullet1 = StringField('One sentence about your duties', validators=[Length(min=20, max=150)])
            bullet2 = StringField('One sentence about your duties', validators=[Length(min=20, max=150)])
            bullet3 = StringField('One sentence about your duties', validators=[Length(min=20, max=150)])
        }
        experience3 = {
            name = StringField('Your employer')
            place = StringField('Where you worked')
            startDate = StringField('Month and year you started')
            endDate = StringField('Month and you ended. If still working, write Present')
            position = StringField('What you worked as')
            bullet1 = StringField('One sentence about your duties', validators=[Length(min=20, max=150)])
            bullet2 = StringField('One sentence about your duties', validators=[Length(min=20, max=150)])
            bullet3 = StringField('One sentence about your duties', validators=[Length(min=20, max=150)])
        }
    }
    Projects = {
        project1 = {
            name = StringField('What the project is called', validators=[DataRequired()])
            place = StringField('Where you worked on it', validators=[DataRequired()])
            startDate = StringField('Month and year you started', validators=[DataRequired()])
            endDate = StringField('Month and you ended. If still working, write Present', validators=[DataRequired()])
            technologies = StringField('What you used to make it', validators=[DataRequired()])
            bullet1 = StringField('One sentence about the project', validators=[DataRequired(), Length(min=20, max=150)])
            bullet2 = StringField('One sentence about the project', validators=[DataRequired(), Length(min=20, max=150)])
            bullet3 = StringField('One sentence about the project', validators=[DataRequired(), Length(min=20, max=150)])
        }
        project2 = {
            name = StringField('What the project is called'])
            place = StringField('Where you worked on it')
            startDate = StringField('Month and year you started')
            endDate = StringField('Month and you ended. If still working, write Present')
            technologies = StringField('What you used to make it')
            bullet1 = StringField('One sentence about the project', validators=[Length(min=20, max=150)])
            bullet2 = StringField('One sentence about the project', validators=[Length(min=20, max=150)])
            bullet3 = StringField('One sentence about the project', validators=[Length(min=20, max=150)])
        }
        project3 = {
            name = StringField('What the project is called'])
            place = StringField('Where you worked on it')
            startDate = StringField('Month and year you started')
            endDate = StringField('Month and you ended. If still working, write Present')
            technologies = StringField('What you used to make it')
            bullet1 = StringField('One sentence about the project', validators=[Length(min=20, max=150)])
            bullet2 = StringField('One sentence about the project', validators=[Length(min=20, max=150)])
            bullet3 = StringField('One sentence about the project', validators=[Length(min=20, max=150)])
        }
    } """