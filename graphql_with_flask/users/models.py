from config import db, bcrypt

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

    def __repr__(self):
        return '<User %r>' % self.email