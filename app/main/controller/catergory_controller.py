from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import CatergoryDto
from ..service.catergory_service import save_new_catergory, get_all_catergories, get_a_catergory, del_a_catergory,update_catergory

api = CatergoryDto.api
_category = CatergoryDto.catergory

@api.route('/')
class CategoryList(Resource):
    @api.doc('list_of_catergories')

    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all catergories"""
        return get_all_catergories()

    @api.expect(_category, validate=True)
    @api.response(201, 'Catergory successfully created.')
    @api.doc('create a new Catergory')
    def post(self):
        """Creates a new Catergory """
        data = request.json
        return save_new_catergory(data=data)


@api.route('/<id>')
@api.param('id', 'The Catergory identifier')
@api.response(404, 'Catergory not found.')
class Catergory(Resource):
    @api.doc('get a Catergory')
    @api.marshal_with(_category)
    def get(self, id):
        """get a Catergory given its identifier"""
        catergory = get_a_catergory(id)
        if not catergory:
            api.abort(404)
        else:
            return catergory

    @api.doc('delete a catergory')
    def delete(self, id):
        """delete a catergory given its identifier"""
        catergory = get_a_catergory(id)
        if not catergory:
            api.abort(404)
        else:
            del_a_catergory(id)
            response_object = {
            'status': 'success',
            'message': 'Catergory successfully deleted.',
            }
            return response_object

    @api.expect(_category, validate=True)
    @api.doc('update a catergory')
    def put(self, id):
        """update a catergory given its identifier"""
        
        catergory = get_a_catergory(id)
        if not catergory:
            api.abort(405)
        else:
            data = request.json
            return update_catergory(id=id, data=data)
            




