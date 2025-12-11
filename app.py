import os
import sqlite3
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuración
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs('uploads', exist_ok=True)

# --- ESTO ES LO QUE TE FALTABA ---
def init_db():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            peso REAL,
            foto TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Ejecutamos la función para crear la base de datos
init_db()
# ---------------------------------

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/subir', methods=['POST'])
def subir_datos():
    peso = request.form['peso']
    if 'foto' not in request.files: return "Sin foto"
    f = request.files['foto']
    
    if f.filename != '':
        nombre = secure_filename(f.filename)
        ruta_foto = os.path.join(app.config['UPLOAD_FOLDER'], nombre)
        f.save(ruta_foto)
        
        # Guardar en Base de Datos
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registros (peso, foto) VALUES (?, ?)", (peso, nombre))
        conn.commit()
        conn.close()
        
        return "<h1>¡Guardado en DB!</h1><a href='/'>Volver</a>"

    return "Error"

if __name__ == '__main__':
    app.run(debug=True)
    