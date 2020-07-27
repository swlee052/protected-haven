from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField

class ReportForm(FlaskForm):
    name = StringField("name")
    email = StringField("email")
    phone = StringField("phone")
    details = TextAreaField("details")
    location = HiddenField("location")