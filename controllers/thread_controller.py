
from flask import Blueprint, render_template

thread_blueprint = Blueprint('thread', __name__)

@thread_blueprint.route('/')
def index():
    # Logica del controller per la pagina principale di Thread
    return render_template('thread_index.html')
