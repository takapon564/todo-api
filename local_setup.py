from flask import Flask
from flask_restful import Resource, Api
from resources.todo import Todo, TodoList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(Todo, '/todos/<string:title>')
api.add_resource(TodoList, '/todos')

if __name__ == "__main__":
    from db import db
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run(port=5000)