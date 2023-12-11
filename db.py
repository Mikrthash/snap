import mysql.connector
from mysql.connector import errorcode

# Configura la connessione al database MySQL
db_config = {
    "host": "localhost",
    "user": "snap",
    "password": "ciaociao",
    "database": "snap"
}

try:
    conn = mysql.connector.connect(**db_config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Errore: Accesso negato")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Errore: Database non esiste")
    else:
        print(err)

# Crea una tabella 'users'
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
"""

# Crea una tabella 'user_activities'
create_user_activities_table = """
CREATE TABLE IF NOT EXISTS user_activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    ip_address VARCHAR(15),
    tweet_count INT DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
"""

# Esegui le query per creare le tabelle
try:
    cursor = conn.cursor()
    cursor.execute(create_users_table)
    cursor.execute(create_user_activities_table)
    conn.commit()
    cursor.close()
except mysql.connector.Error as err:
    print(f"Errore: {err}")

# Chiudi la connessione
conn.close()
