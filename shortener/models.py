from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import random

db = SQLAlchemy()


class Link(db.Model):
    id = db.Column(db.String, primary_key = True)
    link = db.Column(db.String(150), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, link, id = ''):
        self.link = link
        self.id = self.set_id(link)

    # random ass hash function to generate semi-unique id based on url hopefully
    def set_id(self, link):
        initial_hash = link[11:13]
        initial_hash += link[-7:-5]
        initial_hash += str(random.randint(0,99))
        return initial_hash
        