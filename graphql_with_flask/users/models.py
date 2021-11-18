import jwt
from config import db, bcrypt, app

class User(db.Model):
    __tablename__ = 'users'

    def __init__(self, email: str, password: str, active : bool = True):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.active = active

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def check_password(self, password: str):
        return bcrypt.check_password_hash(self.password, password)

    def token_payload(self, ):
        return {
            'uid': self.id,
            'email': self.email, 
        }

    def generate_jwt(self, ) -> str:
        return str(jwt.encode(
            payload=self.token_payload(),
            key=app.config['SECRET_KEY'],
            algorithm='HS256'
        ))

    @classmethod
    def get_user_from_token(cls, jwt_token: str) -> 'User':
        payload = jwt.decode(
            jwt=jwt_token,
            key=app.config['SECRET_KEY'],
            algorithms=['HS256']
        )
        return cls.query.get(payload['uid'])

    def __repr__(self):
        return '<User %r>' % self.email