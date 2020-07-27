from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class ReportForm(FlaskForm):
    name = StringField("name")
    email = StringField("email")
    phone = StringField("phone")
    details = StringField("details")