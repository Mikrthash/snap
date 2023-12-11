from flask import render_template
from . import admin_blueprint  # Importa il blueprint dalla stessa directory

@admin_blueprint.route('/')
def admin_home():
    # La logica per la vista home dell'area amministrativa
    return render_template('admin/home.html')
