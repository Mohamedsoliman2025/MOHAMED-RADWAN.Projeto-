import unittest
from app.models.task_model import TaskModel

class TestTaskModel(unittest.TestCase):

    def setUp(self):
        TaskModel.tasks = []
        TaskModel.current_id = 1

    def test_add_task(self):
        task = TaskModel.add("Test")
        self.assertEqual(task['title'], "Test")
        self.assertEqual(len(TaskModel.tasks), 1)

    def test_update_task(self):
        task = TaskModel.add("Old")
        updated = TaskModel.update(task['id'], "New")
        self.assertEqual(updated['title'], "New")

    def test_delete_task(self):
        task = TaskModel.add("Delete me")
        success = TaskModel.delete(task['id'])
        self.assertTrue(success)
        self.assertEqual(len(TaskModel.tasks), 0)

    def test_get_all(self):
        TaskModel.add("A")
        TaskModel.add("B")
        self.assertEqual(len(TaskModel.get_all()), 2)

if __name__ == '__main__':
    unittest.main()