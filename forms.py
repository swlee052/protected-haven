from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, HiddenField

class ReportForm(FlaskForm):
    name = StringField("name")
    email = StringField("email")
    phone = StringField("phone")
    details = TextAreaField("details")
    send_location = BooleanField("send_location")
    location = HiddenField("location")