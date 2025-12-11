import os
import sqlite3
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

<<<<<<< HEAD
# Configuración
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs('uploads', exist_ok=True)

# --- ESTO ES LO QUE TE FALTABA ---
def init_db():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
=======
# Configuración: Carpeta de fotos
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs('uploads', exist_ok=True)

# --- FUNCIÓN: INICIAR BASE DE DATOS ---
def init_db():
    # Conectamos con el archivo 'datos.db'
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    # Creamos la tabla 'registros' con 4 columnas: id, fecha, peso, foto
>>>>>>> 3aad094a74582c31741a5433f5cb73bed9ce4d49
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

<<<<<<< HEAD
# Ejecutamos la función para crear la base de datos
init_db()
# ---------------------------------
=======
# Ejecutamos esto UNA VEZ al arrancar para asegurar que la tabla exista
init_db()
>>>>>>> 3aad094a74582c31741a5433f5cb73bed9ce4d49

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/subir', methods=['POST'])
def subir_datos():
<<<<<<< HEAD
=======
    # 1. Recibir datos
>>>>>>> 3aad094a74582c31741a5433f5cb73bed9ce4d49
    peso = request.form['peso']
    if 'foto' not in request.files: return "Sin foto"
    f = request.files['foto']
    
    if f.filename != '':
<<<<<<< HEAD
=======
        # 2. Guardar archivo de foto
>>>>>>> 3aad094a74582c31741a5433f5cb73bed9ce4d49
        nombre = secure_filename(f.filename)
        ruta_foto = os.path.join(app.config['UPLOAD_FOLDER'], nombre)
        f.save(ruta_foto)
        
<<<<<<< HEAD
        # Guardar en Base de Datos
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
=======
        # 3. --- GUARDAR EN BASE DE DATOS ---
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()
        # Insertamos el peso y el nombre de la foto
>>>>>>> 3aad094a74582c31741a5433f5cb73bed9ce4d49
        cursor.execute("INSERT INTO registros (peso, foto) VALUES (?, ?)", (peso, nombre))
        conn.commit()
        conn.close()
        
<<<<<<< HEAD
        return "<h1>¡Guardado en DB!</h1><a href='/'>Volver</a>"

    return "Error"
=======
        return "<h1>¡Guardado en Base de Datos!</h1><p>Tu progreso ha sido registrado.</p><a href='/'>Volver</a>"

    return "Error al subir"
>>>>>>> 3aad094a74582c31741a5433f5cb73bed9ce4d49

if __name__ == '__main__':
    app.run(debug=True)
    