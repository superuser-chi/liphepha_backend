from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import ArticleDto,CatergoryDto
from ..service.article_service import save_new_article,update_article,get_all_articles_from
from ..service.article_service import  get_all_articles, get_a_article,del_a_article
api = ArticleDto.api
_article = ArticleDto.article
_category = CatergoryDto.catergory



@api.route('/')
class articleList(Resource):
    @api.doc('list_all_articleed_content')
    @api.marshal_list_with(_article, envelope='data')
    def get(self):
        """List all articleed content"""
        return get_all_articles()

    @api.expect(_article, validate=True)
    @api.response(201, 'article was successfully created.')
    @api.doc('create a new article')
    def post(self):
        """Creates a new article """
        data = request.json
        return save_new_article(data=data)

@api.route('/<catergory>')
@api.param('catergory', 'The article Category identifier')
class articleListFrom(Resource):
    @api.doc('list_all_articled_content')
    @api.marshal_list_with(_article, envelope='data')
    def get(self, catergory):
        """List all articleed content from a category"""
        return get_all_articles_from(catergory)

@api.route('/<id>')
@api.param('id', 'The article identifier')
class article(Resource):
    @api.doc('get a article')
    @api.marshal_with(_article)
    def get(self, id):
        """get a article given its identifier"""
        article = get_a_article(id)
        if not article:
            api.abort(404)
        else:
            return article

    @api.doc('delete a article')
    def delete(self, id):
        """delete a article given its identifier"""
        article = get_a_article(id)
        if not article:
            api.abort(404)
        else:
            del_a_article(id)
            response_object = {
            'status': 'success',
            'message': 'article successfully deleted.',
            }
            return response_object

    @api.expect(_article, validate=True)
    @api.doc('update a article')
    def put(self, id):
        """update a article given its identifier"""
        user = get_a_article(id)
        if not user:
            api.abort(404)
        else:
            data = request.json
            return update_article(id=id,data=data)



