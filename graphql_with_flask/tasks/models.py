import enum
from config import db
from sqlalchemy_utils.types.choice import ChoiceType
from users.models import User

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.__tablename__ + '.id'), nullable=False)
    user = db.relationship('User', backref=db.backref(__tablename__, lazy=True))

    class TaskStatus(enum.Enum):
        NOTSTARTED = 'NOTSTARTED'
        INPROGRESS = 'INPROGRESS'
        DONE = 'DONE'

    status = db.Column(ChoiceType(TaskStatus, impl=db.String(16)), nullable=False, default=TaskStatus.NOTSTARTED)
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<Task %r>' % self.id