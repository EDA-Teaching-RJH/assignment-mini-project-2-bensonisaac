import unittest
from task_manager import TaskManager, Task
# tests to make sure everthing works as expected in task manager 
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager("test_tasks.csv")
# test if adding a task works 
    def test_add_task(self):
        self.manager.add_task("Buy groceries", "High")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Buy groceries")
# tests if marking a task as complete works
    def test_mark_task_complete(self):
        self.manager.add_task("Wash the car", "Medium")
        self.assertTrue(self.manager.mark_task_complete("Wash the car"))
        self.assertTrue(self.manager.tasks[0].completed)
# test for marking non existent task as complete returns as false 
    def test_mark_task_complete_not_found(self):
        self.manager.add_task("Read a book", "Low")
        self.assertFalse(self.manager.mark_task_complete("Go jogging"))
#tests if saving and loading tasks works
    def test_save_and_load_tasks(self):
        self.manager.add_task("Task 1", "High")
        self.manager.save_tasks()

        new_manager = TaskManager("test_tasks.csv")
        new_manager.load_tasks()
        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0].description, "Task 1")
        self.assertEqual(new_manager.tasks[0].priority, "High")

if __name__ == "__main__":
    unittest.main() # runs all tests