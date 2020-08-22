from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

#the basic class of objects in our database for each available language
class Lang(db.Model):
    """Info for languages"""
    
    __tablename__ = 'langs'

    # id = db.Column(db.Integer,
    #                 primary_key=True,
    #                 autoincrement=True)
    name = db.Column(db.String(), 
                        primary_key=True)
    script = db.Column(db.String, nullable=False)
    form_name = db.Column(db.String, nullable=False)
    form_email = db.Column(db.String, nullable=False)
    form_phone = db.Column(db.String, nullable=False)
    form_details = db.Column(db.String, nullable=False)
    form_geoloc = db.Column(db.String, nullable=False)
    form_personal_info = db.Column(db.String, nullable=False)
    form_call_notice = db.Column(db.String, nullable=False)
    form_incident_details = db.Column(db.String, nullable=False)
    form_submit = db.Column(db.String, nullable=False)
    form_cancel = db.Column(db.String, nullable=False)
    form_resources = db.Column(db.String, nullable=False)
    form_no_geo = db.Column(db.String, nullable=False)
    resources = db.relationship('Resource',
                                backref='lang', cascade="all,delete")

##make categories table?

class Resource(db.Model):
    """resource database"""

    __tablename__ = 'resources'

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    lang_id = db.Column(db.String, db.ForeignKey('langs.name'))
    category = db.Column(db.String)
    title = db.Column(db.String)
    text =  db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)

# class Category(db.Model):
#     """resource categories"""

#     id = db.Column(db.Integer,
#                     primary_key = True,
#                     autoincrement = True)


# class Admin(db.Model):
#     """admin login info"""

#     __tablename__ = 'admins'

#     id = db.Column(db.Integer,
#                     primary_key=True,
#                     autoincrement=True)
#     username = db.Column(db.String, nullable=False, unique=True)
#     password = db.Column(db.Text, nullable=False)

#     @classmethod
#     def admin_reg(cls, username, pwd):
#         """Register admin with hashed password"""

#         hashed = bcrypt.generate_password_hash(pwd)

#         hashed_utf8 = hashed.decode("utf8")

#         return cls(username=username, password=hashed_utf8)

#     @classmethod
#     def auth_admin(cls, username, password):
#         """Authenticates the admin login"""

#         user = User.query.filter_by(username)

#         if user and bcrypt.check_password_hash(user.password, password):
#             return user
#         else:
#             return False