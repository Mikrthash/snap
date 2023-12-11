from flask import render_template, request, redirect, url_for
from . import users

@users.route('/login', methods=['GET', 'POST'])
def login():
    # Logica per il login
    return render_template('login.html')

@users.route('/register', methods=['GET', 'POST'])
def register():
    # Logica per la registrazione
    return render_template('register.html')

# Altre funzioni relative agli utenti...
