from datetime import datetime
from __int__ import db
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    id = Column(Integer, primary_key=True)
    image = Column(String(20), unique=True)
    image_file = Column(String(20), default='default.jpg')
    password = Column(String(60), unique=True)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = Column(db.Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime(), nullable=False, default=datetime.utcnow)
    content = Column(Text(), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.username}', '{self.date_posted}')"
