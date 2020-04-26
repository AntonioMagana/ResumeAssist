from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

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
        schoolGPA=StringField('School GPA',  validators=[DataRequired(), Length(min =1, max=6)])
        schoolStartDate=StringField('Start Date', validators=[DataRequired(), Length(min =3, max=40)])
        schoolEndDate=StringField('End Date', validators=[DataRequired(), Length(min =3, max=40)])
        schoolCourse1=StringField('Relevant Course', validators=[DataRequired(), Length(min =3, max=40)])
        schoolCourse1Description=TextAreaField('Relevant Course Description', validators=[DataRequired(), Length(min =3, max=100)])
        schoolCourse2=StringField('Relevant Course')
        schoolCourse2Description=TextAreaField('Relevant Course Description')
        schoolCourse3=StringField('Relevant Course')
        schoolCourse3Description=TextAreaField('Relevant Course Description')

        projectTitle = StringField('Project Title', validators=[DataRequired(), Length(min =3, max=40)])
        projectDescription = TextAreaField('Project Description', validators=[DataRequired(), Length(min =10, max=500)])
        projectTime = StringField('Time Frame', validators=[DataRequired(), Length(min =3, max=40)])

        projectTitle2 = StringField('Project Title', validators=[Optional()])
        projectDescription2 = TextAreaField('Project Description')
        projectTime2 = StringField('Time Frame')

        projectTitle3 = StringField('Project Title')
        projectDescription3 = TextAreaField('Project Description')
        projectTime3 = StringField('Time Frame')

        workTitle = StringField('Work title', validators=[DataRequired(), Length(min =3, max=40)])
        workCompany = StringField("Company",validators=[DataRequired(), Length(min =3, max=40)])
        workDescription = TextAreaField('Work Description', validators=[DataRequired(), Length(min =10, max=100)])
        workStartDate = StringField('Work Start Date', validators=[DataRequired(), Length(min =3, max=40)])
        workEndDate = StringField('Work End Date', validators=[DataRequired(), Length(min =3, max=40)])

        workTitle2 = StringField('Work title', validators=[Optional()])
        workCompany2 = StringField("Company", validators=[Optional()])
        workDescription2 = TextAreaField('Work Description', validators=[Optional()])
        workStartDate2 = StringField('Work Start Date', validators=[Optional()])
        workEndDate2 = StringField('Work End Date', validators=[Optional()])

        workTitle3 = StringField('Work title', validators=[Optional()])
        workCompany3 = StringField("Company", validators=[Optional()])
        workDescription3 = TextAreaField('Work Description', validators=[Optional()])
        workStartDate3 = StringField('Work Start Date', validators=[Optional()])
        workEndDate3 = StringField('Work End Date', validators=[Optional()])

    #submit = SubtmitField('Submit')
