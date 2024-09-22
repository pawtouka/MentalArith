from datetime import datetime
import os
import binascii
from ..extensions import db
from ..functions import generate_queue_def, generate_queue_bro

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    topic = db.Column(db.String(250))
    maximum = db.Column(db.Integer)
    actions = db.Column(db.Integer)
    dignits = db.Column(db.Integer)
    queue = db.Column(db.Text)
    res = db.Column(db.Text)
    random_hex = db.Column(db.String(64), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, teacher, topic, maximum, actions, dignits):
        self.teacher = teacher
        self.topic = topic
        self.maximum = maximum
        self.actions = actions
        self.dignits = dignits

        # Генерация queue и res при создании постера
        if topic == 'просто':
            self.queue, self.res, self.random_hex = generate_queue_def(int(actions), int(maximum), int(dignits))
        elif topic == 'брат':
            self.queue, self.res, self.random_hex = generate_queue_bro(int(actions), 9, int(dignits), int(maximum))
