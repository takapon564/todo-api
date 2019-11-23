from models.todo import TodoModel
from tests.base_test import BaseTest

import json


class TodoTest(BaseTest):

    def test_find_todo(self):
        with self.app() as c:
            with self.app_context():
                TodoModel('task1', 'shopping').save_to_db()
                r = c.get('todos/task1')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'title': 'task1', 'content': 'shopping'},
                                     d2=json.loads(r.data))

    def test_delete_todo(self):
        with self.app() as c:
            with self.app_context():
                TodoModel('task1', 'shopping').save_to_db()
                r = c.delete('/todos/task1')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'message': 'Todo deleted'},
                                     d2=json.loads(r.data))

    def test_create_todo(self):
        with self.app() as c:
            with self.app_context():
                r = c.post('/todos/task1', data={'content': 'shopping'})
                self.assertEqual(r.status_code, 201)
                self.assertEqual(TodoModel.find_by_title('task1').content, 'shopping')
                self.assertDictEqual(d1={'title': 'task1', 'content': 'shopping'},
                                     d2=json.loads(r.data))

    def test_duplicate_todo(self):
        with self.app() as c:
            with self.app_context():
                c.post('/todos/task1', data={'content': 'shopping'})
                r = c.post('/todos/task1', data={'content': 'shopping'})

                self.assertEqual(r.status_code, 400)
            
    def test_put_item(self):
       with self.app() as c:
            with self.app_context(): 
                r = c.put('/todos/task1', data={'content': 'shopping'})

                self.assertEqual(r.status_code, 200)
                self.assertEqual(TodoModel.find_by_title('task1').content, 'shopping')
                self.assertDictEqual(d1={'title': 'task1', 'content': 'shopping'},
                                     d2=json.loads(r.data))

    def test_put_update_item(self):
        with self.app() as c:
            with self.app_context():
                c.put('/todos/task1', data={'content': 'shopping'})
                r = c.put('/todos/task1', data={'content': 'walking'})

                self.assertEqual(r.status_code, 200)
                self.assertEqual(TodoModel.find_by_title('task1').content, 'walking')



                
if __name__ == "__main__":
    BaseTest.unittest.main()