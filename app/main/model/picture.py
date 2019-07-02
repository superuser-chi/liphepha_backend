from ..import db
import datetime


class Picture(db.Model):
    """
    Cartegory Model for storing pictures on an article
    """
    __tablename__ = 'pictures'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    caption = db.Column(db.String(50),  nullable=False)
    path = db.Column(db.String(1000),  nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

    def __init__(self, caption, path):
        self.caption = caption
        self.path = path

    def __repr__(self):
        return '<id: name: {}'.format(self.caption)

