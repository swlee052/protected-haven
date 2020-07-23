from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Lang(db.Model):
    __tablename__ = 'langs'
    # id = db.Column(db.Integer,
    #                 primary_key=True,
    #                 autoincrement=True)
    name = db.Column(db.String(), 
                        primary_key=True)
    script = db.Column(db.String(), nullable=False)
    report = db.Column(db.Integer(), db.ForeignKey('report.id'))
#   resources = db.Column(db.Integer(), db.ForeignKey('resources.id'))

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)         
    name = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=True)
    phone = db.Column(db.String(), nullable=True)
    detail = db.Column(db.String(), nullable=True)

# class Resource(db.Model):
#      __tablename__ = 'resources'
#     id = db.Column(db.Integer,
#                     primary_key = True,
#                     autoincrement = True)         
