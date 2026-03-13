from flask import Blueprint

inicio=Blueprint(
    'inicio',
    __name__,
    template_folder='templates',
    static_folder='static')
from . import routes