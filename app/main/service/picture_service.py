import uuid
import datetime

from app.main import db
from app.main.model.picture import Picture
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def save_new_picture(data):
    picture = Picture.query.filter_by(caption=data['caption']).first()
    article = Article.query.filter_by(caption=data['article_id']).first()
    if not picture and article:
        new_picture = Picture(
            caption=data['caption'],
            path=data['path'],
            article_id=article.id
        )
        save_changes(new_picture)
        response_object = {
            'status': 'success',
            'message': 'picture successfully added',
        }
        return response_object, 404
    else:
        response_object = {
            'status': 'fail',
            'message': 'picture already exists',
        }
        return response_object, 404

def update_picture (id,data):
    picture = Picture.query.filter_by(id=id).first()
    if not picture :
        response_object = {
            'status': 'fail',
            'message': 'picture does not exists',
        }
        return response_object, 404
    else:
        picture.caption = data['caption']
        picture.path = data['path']    
        db.session.merge(picture)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'picture successfully updated',
        }
        return response_object, 200


def get_all_pictures():
    return Picture.query.all()

def get_a_picture(id):
    return Picture.query.filter_by(id=id).first()

def del_a_picture(id):
    picture = picture.query.filter_by(id=id).first()
    db.session.delete(picture)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

