# app.py

from flask import Flask

# Creamos la aplicación
app = Flask(__name__)

# Esto define la página principal (la 'ruta' inicial)
@app.route('/')
def inicio():
    return "<h1>¡Hola! Esta es mi App de Personal Trainer</h1><p>Estamos en construcción.</p>"

# Esto enciende el servidor
if __name__ == '__main__':
    app.run(debug=True)
