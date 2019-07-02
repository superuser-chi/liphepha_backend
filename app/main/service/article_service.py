import uuid
import datetime

from app.main import db
from app.main.model.article import Article
from app.main.model.user import User
from app.main.model.catergory import Catergory

def save_new_article(data):
    auth_token = data['Authorization']
    user = User.query.filter_by(id=User.decode_auth_token(auth_token)).first()
    article = Article.query.filter_by(title=data['title']).first()
    catergory = Catergory.query.filter_by(id=data['catergory_id']).first()
    if user and catergory:
        if not article:
            new_article = Article(
                title=data['title'],
                content=data['content'],
                catergory=catergory.id,
                posted_by=user.id
            )
            user.articles.append(new_article)
            db.session.merge(user)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'article has been successfully created.',
            }
            return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'article already exists',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'user or Catergory does not exists',
        }
        return response_object, 409        

def update_article(public_id,data):
    auth_token = data['Authorization']
    user = User.query.filter_by(id=User.decode_auth_token(auth_token))
    
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'user article does not exists',
        }
        return response_object, 404
    else:
        article = Article.query.filter_by(public_id=public_id).first()
        if not article:
            response_object = {
                'status': 'fail',
                'message': 'article does not exists',
            }
            return response_object, 404
        else:
            catergory = Catergory.query.filter_by(title=data['name']).first()
            if catergory:
                article.title = data['title']
                article.category = data['category']
                article.contents = data['contents']
                db.session.merge(article)
                db.session.commit()
                response_object = {
                    'status': 'success',
                    'message': 'article was successfully updated',
                }
                return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'article category does not exists',
                }
                return response_object, 404

def del_a_article(id):
    article = Article.query.filter_by(id=id).first()
    db.session.delete(article)
    db.session.commit()

def get_all_articles():
    return Article.query.all()

def get_all_articles_from(name):
    catergory = Catergory.query.filter_by(name=name).first()
    if catergory:
        return Article.query.filter_by(catergory_id=catergory.id).all()
    else:
        response_object = {
                    'status': 'fail',
                    'message': 'article category does not exists',
                }
        return response_object, 404

def get_a_article(id):
    return Article.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

