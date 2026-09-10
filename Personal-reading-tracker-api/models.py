from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
 
    reading_entries = db.relationship(
        'ReadingEntry',
        back_populates='user',
        cascade='all, delete-orphan'
    )
    def __repr__(self):
        return f'<User {self.username}>'