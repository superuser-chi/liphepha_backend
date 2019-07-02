from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import PictureDto
from ..service.picture_service import save_new_picture, get_all_pictures, get_a_picture, del_a_picture,update_picture

api = PictureDto.api
_picture = PictureDto.picture

@api.route('/')
class pictureList(Resource):
    @api.doc('list_of_catergories')

    @api.marshal_list_with(_picture, envelope='data')
    def get(self):
        """List all catergories"""
        return get_all_catergories()

    @api.expect(_picture, validate=True)
    @api.response(201, 'picture successfully created.')
    @api.doc('create a new picture')
    def post(self):
        """Creates a new picture """
        data = request.json
        return save_new_picture(data=data)


@api.route('/<id>')
@api.param('id', 'The picture identifier')
@api.response(404, 'picture not found.')
class picture(Resource):
    @api.doc('get a picture')
    @api.marshal_with(_picture)
    def get(self, id):
        """get a picture given its identifier"""
        picture = get_a_picture(id)
        if not picture:
            api.abort(404)
        else:
            return picture

    @api.doc('delete a picture')
    def delete(self, id):
        """delete a picture given its identifier"""
        picture = get_a_picture(id)
        if not picture:
            api.abort(404)
        else:
            del_a_picture(id)
            response_object = {
            'status': 'success',
            'message': 'picture successfully deleted.',
            }
            return response_object

    @api.expect(_picture, validate=True)
    @api.doc('update a picture')
    def put(self, id):
        """update a picture given its identifier"""
        
        picture = get_a_picture(id)
        if not picture:
            api.abort(405)
        else:
            data = request.json
            return update_picture(id=id, data=data)
            




