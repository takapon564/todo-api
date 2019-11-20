import sqlite3
from flask_restful import Resource, reqparse
from models.todo import TodoModel

class Todo(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('content',
        type=str,
        required=True,
        help='Content cannnot be left blank!'
    )

    def get(self, title):
        todo = TodoModel.find_by_title(title)
        if todo:
            return todo.json()
        return {'message': 'Todo not found.'}, 404
    
    def post(self, title):
        if TodoModel.find_by_title(title):
            return {'message': "the todo '{}' already exists".format(title)}, 400

        data = Todo.parser.parse_args()

        todo = TodoModel(title, data['content'])

        try:
            todo.save_to_db()
        except:
            return {"message": "An error occurred inserting the todo."}, 500

        return todo.json(), 201

    def delete(self, title):
        todo = TodoModel.find_by_title(title)
        if todo:
            todo.delete_from_db()
        return {"message": "Todo deleted"}