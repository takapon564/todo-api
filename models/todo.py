import sqlite3
from db import db

class TodoModel(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(80))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {'title': self.title, 'content': self.content}

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()