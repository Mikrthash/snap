from flask import Flask,render_template

from admin.views import admin_blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Sostituisci 'index.html' con il nome del tuo file HTML

if __name__ == '__main__':
    app.run(debug=True)

app = Flask("SnapThread")  # Imposta il nome dell'app su "SnapThread"

# Registra i Blueprint
app.register_blueprint(admin_blueprint, url_prefix='/index')
# Aggiungi qui la registrazione di altri Blueprint

if __name__ == '__main__':
    app.run(debug=True)
