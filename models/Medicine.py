from VetLife import db
from .BaseModel import BaseModel


class Medicine(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    descr = db.Column(db.String(1024))

    def __repr__(self):
        return self.title
