from tests.base_test import BaseTest

from  models.todo import TodoModel

class TodoTest(BaseTest):

    def test_todoのインスタンスが作成されること(self):
        todo = TodoModel('task1', 'walking')

        self.assertEqual(todo.title, 'task1')
        self.assertEqual(todo.content, 'walking')

    def test_todoの情報がjsonで返却される(self):
        todo = TodoModel('task1', 'waking')
        expected = {
            'title': 'task1',
            'content': 'waking'
        }
        self.assertEqual(todo.json(), expected)
