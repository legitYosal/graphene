from config import db, User
from .base import BaseTest

class TestUserJWT(BaseTest): 
    
    def test_user_jwt(self, ):
        email = 'flaslnm@gmail.com'
        password = '123'
        my_user = User(email, password)
        db.session.add(my_user)
        db.session.commit()

        user_token = my_user.generate_jwt()

        user = User.get_user_from_token(jwt_token=user_token)
        self.assertEqual(my_user.email, user.email)