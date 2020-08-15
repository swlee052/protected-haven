from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    form_name = db.Column(db.String, nullable=True)
    form_email = db.Column(db.String, nullable=True)
    form_phone = db.Column(db.String, nullable=True)
    form_details = db.Column(db.String, nullable=True)
    form_geoloc = db.Column(db.String, nullable=True)
    resources = db.relationship('Resource',
                                backref='lang', cascade="all,delete")

class Resource(db.Model):
    """resource database"""

    __tablename__ = 'resources'

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    lang_id = db.Column(db.String, db.ForeignKey('langs.name'))
    text =  db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    email = db.Column(db.String)
