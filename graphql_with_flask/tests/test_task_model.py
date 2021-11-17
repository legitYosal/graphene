from datetime import datetime
from config import db
from .base import BaseTest
from users.models import User
from tasks.models import Task

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