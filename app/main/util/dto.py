from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'firstname': fields.String(required=True, description='user username'),
        'lastname': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'phone': fields.String(required=True, description='user cellphone number'),
        'public_id': fields.String(description='user Identifier')
    })
    user2 = api.model('user2', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'firstname': fields.String(required=True, description='user username'),
        'lastname': fields.String(required=True, description='user username'),
        'phone': fields.String(required=True, description='user celllphone number'),
        'old_password': fields.String(required=True, description='user password'),
        'password': fields.String(required=True, description='user password'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class CatergoryDto:
    api = Namespace('catergory', description='catergory related operations')
    catergory = api.model('auth_details', {
        'name': fields.String(required=True, description='The catergory name'),
    })

class ArticleDto:
    api = Namespace('article', description='article related operation')
    article = api.model('article_details', {
        'Authorization': fields.String(required=True, description="The authentication token"),
        'title': fields.String(required=True, description="The article title"),
        'catergory_id': fields.String(required=True, description="The article category"),
        'content': fields.String(required=True, description="The article content"),
        'posted_by': fields.String(required=True, description="The article content"),
        'id': fields.String(required=True, description="The article identifier"),
    })

class PictureDto:
    api = Namespace('picture', description='picture related operations')
    picture = api.model('auth_details', {
        'caption': fields.String(required=True, description='The picture caption'),
        'path': fields.String(required=True, description='The picture path'),
        'article_id': fields.String(required=True, description="The article identifier to which the picture belongs to"),
    })
