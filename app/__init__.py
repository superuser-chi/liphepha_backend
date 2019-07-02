from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.catergory_controller import api as catergory_ns
from .main.controller.article_controller import api as article_ns
from .main.controller.picture_controller import api as picture_ns
blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Liphephandzaba API',
          version='1.0',
          description='This is a web service for the Liphephandzaba application'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(catergory_ns, path='/categories')
api.add_namespace(article_ns, path='/article')
api.add_namespace(picture_ns, path='/picture')

