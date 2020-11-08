from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(32))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(32))

    def __repr__(self):
        return '<User %r>' % self.username
