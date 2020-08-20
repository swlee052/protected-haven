from flask import Flask, render_template, redirect, flash
from models import connect_db, Lang, Admin
from forms import ReportForm, LoginForm
from flask_mail import Mail, Message
from datetime import datetime
# import stdiomask

# username = input("Enter PostgreSQL username: ") #postgres
# password = stdiomask.getpass("Enter Password: ")

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost/protected_haven'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///protected_haven'
app.config['SQLALCHEMY-TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


"""Mail configuration"""
app.config['MAIL_SERVER']='protectedhaven.space'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'report@protectedhaven.space'
app.config['MAIL_PASSWORD'] = 'wewillbeyouradvocate'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'whateveryouwant'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#sets up and renders a homepage with all buttons in the database
@app.route('/')
def home():
    langs = Lang.query.all()
    return render_template('index.html', langs=langs)

@app.route('/action/<lang>')
def action(lang): 
    return

@app.route('/report/<lang>', methods=["GET", "POST"]) 

#Sets up and displays a report form in the selected language
def report(lang):
    lang = Lang.query.get_or_404(lang)

#creates form from forms.py, adds the appropriate language labels
    form = ReportForm()
    form.name.label = lang.form_name
    form.phone.label = lang.form_phone
    form.details.label = lang.form_details
    form.email.label = lang.form_email
    form.send_location.label = lang.form_geoloc

    if form.validate_on_submit(): 
        name = form.name.data if form.name.data else 'Unspecified'
        phone = form.phone.data if form.phone.data else 'Unspecified'
        details = form.details.data if form.details.data else 'Unspecified'
        email = form.email.data if form.email.data else 'Unspecified'
        if form.send_location.data == True:
            location = "User did not wish to share their geodata"
        else:
            location = form.location.data

        # print(name, phone, details, email, location)

        """send email to the police"""
        time_obj = datetime.now()
        msg_time = str(time_obj.year) + '/' + str(time_obj.month) + '/' + str(time_obj.day) + '-' + str(time_obj.hour) + ':' + str(time_obj.minute)

        msg = Message(f'New Report from Protected Haven: {msg_time}', 
                        sender = 'report@protectedhaven.space', 
                        recipients = ['report@protectedhaven.space'])
        msg.body = "{name} {phone} {details} {email} {locations}"
        mail.send(msg)
        return "Sent"


        return render_template('confirmation.html')

    # import pdb
    # pdb.set_trace()
    return render_template('report.html', lang=lang, form=form)

@app.route('/resources/<lang>', methods=["GET"]) 
def resources(lang):
    lang = Lang.query.get_or_404(lang)
    return render_template('resources.html', lang=lang)

# @app.route('/confirmation/<lang>')
# def confirmation(lang): 
#     return

# @app.route('/error/<lang>')
# def error(lang):
#     return

# @app.route('/admin_login', methods=["GET", "POST"])
# def admin():

#     form = LoginForm()

#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data

#         admin = Admin.auth_admin(username, password)
#         if admin:
#             session["user_id"] = user.id
#             return redirect("/admin_menu")
#         else:
#             form.username.errors = ["There's a problem with your username."]
#             form.password.errors = ["There's a problem with your password."]


#     return render_template("admin.html", form=form)


#     @app.route('/admin_menu', methods=["GET", "POST"])
#     def admin_menu():

#         if "user_id" not in session:
#             flash("You must be logged in to view!")
#             return redirect("/")

#         else:

#             return render_template('admin-menu.html')
