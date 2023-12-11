import os

def create_controller_folder():
    try:
        os.makedirs("controllers")
        print("Cartella 'controllers' creata.")
    except FileExistsError:
        print("La cartella 'controllers' esiste già.")

def create_controller_file(controller_name):
    controller_content = f"""
from flask import Blueprint, render_template

{controller_name.lower()}_blueprint = Blueprint('{controller_name.lower()}', __name__)

@{controller_name.lower()}_blueprint.route('/')
def index():
    # Logica del controller per la pagina principale di {controller_name}
    return render_template('{controller_name.lower()}_index.html')
"""

    file_name = f"controllers/{controller_name.lower()}_controller.py"
    with open(file_name, "w") as file:
        file.write(controller_content)

    print(f"Creato il file {file_name}")

if __name__ == "__main__":
    create_controller_folder()

    # Aggiungi i nomi dei controller che desideri creare
    controller_names = ["Thread", "User", "Auth", "Admin", "Message", "File", "Notification"]

    for name in controller_names:
        create_controller_file(name)


