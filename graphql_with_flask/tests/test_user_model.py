from .base import BaseTest
from config import bcrypt, db, User

class TestUser(BaseTest):

    def test_user_creation(self, ):
        self.assertTrue(True)
        password = '123'
        email = 'test@gmail.com'
        user = User(email, password)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=email).first()
        self.assertTrue(bcrypt.check_password_hash(user.password, password))

