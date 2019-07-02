import uuid
import datetime

from app.main import db
from app.main.model.catergory import Catergory


def save_new_catergory(data):
    catergory = Catergory.query.filter_by(name=data['name']).first()
    if not catergory:
        new_catergory = Catergory(
            name=data['name'],
        )
        save_changes(new_catergory)
        response_object = {
            'status': 'success',
            'message': 'Catergory successfully added',
        }
        return response_object, 404
    else:
        response_object = {
            'status': 'fail',
            'message': 'Catergory already exists',
        }
        return response_object, 404

def update_catergory (id,data):
    catergory = Catergory.query.filter_by(id=id).first()
    if not catergory :
        response_object = {
            'status': 'fail',
            'message': 'Catergory does not exists',
        }
        return response_object, 404
    else:
        catergory.name = data['name']
            
        db.session.merge(catergory)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Catergory successfully updated',
        }
        return response_object, 200


def get_all_catergories():
    return Catergory.query.all()

def get_a_catergory(id):
    return Catergory.query.filter_by(id=id).first()

def del_a_catergory(id):
    catergory = Catergory.query.filter_by(id=id).first()
    db.session.delete(catergory)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

