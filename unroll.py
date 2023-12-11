from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configura la connessione al database MySQL
db_config = {
  "host": "localhost",
    "user": "snap",
    "password": "ciaociao",
    "database": "snap"
}

# Crea una connessione MySQL
try:
    conn = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    print(f"Errore di connessione al database: {err}")

# Definisci il modello per l'attività dell'utente
class UserActivity:
    def __init__(self, id, ip_address, tweet_count):
        self.id = id
        self.ip_address = ip_address
        self.tweet_count = tweet_count

@app.route('/view_tweet')
def view_tweet():
    user_ip = request.remote_addr  # Ottieni l'indirizzo IP dell'utente
    cursor = conn.cursor()

    # Esegui una query per recuperare l'attività dell'utente
    cursor.execute("SELECT * FROM user_activities WHERE ip_address = %s", (user_ip,))
    user_activity_data = cursor.fetchone()

    if not user_activity_data:
        # Se l'utente non ha un'attività, inseriscilo nel database
        cursor.execute("INSERT INTO user_activities (ip_address, tweet_count) VALUES (%s, 1)", (user_ip,))
        conn.commit()
        cursor.close()
    else:
        # Altrimenti, aggiorna il conteggio dei tweet visualizzati
        new_tweet_count = user_activity_data[2] + 1
        cursor.execute("UPDATE user_activities SET tweet_count = %s WHERE id = %s", (new_tweet_count, user_activity_data[0]))
        conn.commit()
        cursor.close()

        if new_tweet_count >= 3:
            return redirect(url_for('register'))

    return render_template('tweet.html', tweet_number=new_tweet_count)

@app.route('/register')
def register():
    return "Registrati qui"

if __name__ == "__main__":
    app.run(debug=True)
