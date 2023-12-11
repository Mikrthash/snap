from flask import Blueprint, render_template

# Creazione del Blueprint per la sezione amministrativa
admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/')
def admin_index():
    # Logica per la pagina principale di Admin
    # Qui puoi inserire codice per recuperare dati, verificare sessioni, ecc.
    return render_template('admin_index.html')

# Puoi aggiungere altre route qui
@admin_blueprint.route('/another-page')
def another_page():
    # Logica per un'altra pagina amministrativa
    return render_template('another_page.html')

