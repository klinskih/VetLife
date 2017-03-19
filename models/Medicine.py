# -*- coding: utf-8 -*-
from VetLife import db


class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True, info={'label': u'Наименование'})
    descr = db.Column(db.String(1024), info={'label': u'Описание'})

    def __repr__(self):
        return self.title
