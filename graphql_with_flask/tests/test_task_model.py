from datetime import datetime
from config import db, User, Task
from .base import BaseTest

class TestTask(BaseTest):

    def test_task_creation(self, ):
        user = User('email@gmail.com', '123')
        task = Task(
            title='t',
            user=user,
            due_date=datetime.now()
        )
        db.session.add(user)
        db.session.add(task)
        db.session.commit()
        task = Task.query.first()
        self.assertEqual(task.user.email, user.email)        