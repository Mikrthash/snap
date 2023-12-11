from flask import render_template
from . import admin

@admin.route('/dashboard')
def dashboard():
    # Dashboard dell'amministratore
    return render_template('admin_dashboard.html')

# Altre funzioni di amministrazione...
