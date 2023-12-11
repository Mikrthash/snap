
from flask import Blueprint, render_template

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/')
def index():
    # Logica del controller per la pagina principale di User
    return render_template('user_index.html')
