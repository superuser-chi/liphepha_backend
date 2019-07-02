from ..import db
import datetime


class Article(db.Model):
    """
    Token Model for storing articles
    """
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(50),  nullable=False)
    headline = db.Column(db.String(100),  nullable=False)
    content = db.Column(db.String(1000),  nullable=False)
    is_top_story = db.Column(db.Boolean, nullable=False)
    posted_on = db.Column(db.DateTime, nullable=False)
    modified_on = db.Column(db.DateTime, nullable=False)
    catergory_id =  db.Column(db.Integer, db.ForeignKey('catergories.id'), nullable=False)
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, posted_by,catergory, title,headline, content):
        self.title = title
        self.headline = headline
        self.content = content
        self.posted_on = datetime.datetime.now()
        self.modified_on = datetime.datetime.now()
        self.posted_by = posted_by
        self.catergory_id = catergory

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
