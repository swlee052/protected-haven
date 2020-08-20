from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, HiddenField, PasswordField
from wtforms.validators import InputRequired

class ReportForm(FlaskForm):
    name = StringField("name")
    email = StringField("email")
    phone = StringField("phone")
    details = TextAreaField("details")
    send_location = BooleanField("send_location")
    location = HiddenField("location")

class LoginForm(FlaskForm):

    username = StringField("Username", validators=[InputRequired(message="Please enter your username")])
    password = PasswordField("Password", validators=[InputRequired(message="Please enter your password")])