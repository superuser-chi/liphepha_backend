from ..import db
import datetime


class Catergory(db.Model):
    """
    Cartegory Model for storing article catergories
    """
    __tablename__ = 'catergories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50),  nullable=False)
   

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id: name: {}'.format(self.name)

