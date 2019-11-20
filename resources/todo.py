import sqlite3
from flask_restful import Resource, reqparse
from models.todo import TodoModel

class Todo(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type=str,
        required=True,
        help='Title cannnot be left blank!'
    )

    def get(self, title):
        todo = TodoModel.find_by_title(title)
        if todo:
            return todo.json()
        return {'message': 'Todo not found.'}, 404