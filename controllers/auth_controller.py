from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__)

# Il resto del tuo codice...

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # Logica per mostrare e gestire il form di login
    # ...
    return render_template('login.html')

@auth_blueprint.route('/logout')
def logout():
    # Logica per gestire il logout
    # ...
    return "Logout effettuato"

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # Logica per mostrare e gestire il form di registrazione
    # ...
    return render_template('register.html')

