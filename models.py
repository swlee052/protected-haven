from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#the basic class of objects in our database for each available language
class Lang(db.Model):
    __tablename__ = 'langs'
    # id = db.Column(db.Integer,
    #                 primary_key=True,
    #                 autoincrement=True)
    name = db.Column(db.String(), 
                        primary_key=True)
    script = db.Column(db.String(), nullable=False)
    form_name = db.Column(db.String(), nullable=True)
    form_email = db.Column(db.String(), nullable=True)
    form_phone = db.Column(db.String(), nullable=True)
    form_details = db.Column(db.String(), nullable=True)
    form_geoloc = db.Column(db.String(), nullable=True)
    # report = db.Column(db.Integer(), db.ForeignKey('report.id'))
    # resources = db.Column(db.Integer(), db.ForeignKey('resources.id'))

#unneeded at the moment, may be deleted if not used
# class Report(db.Model):
#     __tablename__ = 'reports'
#     id = db.Column(db.Integer,
#                     primary_key = True,
#                     autoincrement = True)         
#     form_name = db.Column(db.String(), nullable=True)
#     form_email = db.Column(db.String(), nullable=True)
#     form_phone = db.Column(db.String(), nullable=True)
#     form_detail = db.Column(db.String(), nullable=True)

#this will be the class to possibly hold resources in the future
# class Resource(db.Model):
#      __tablename__ = 'resources'
#     id = db.Column(db.Integer,
#                     primary_key = True,
#                     autoincrement = True)         
