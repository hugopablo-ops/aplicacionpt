import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# CONFIGURACIÓN: Carpeta donde caerán las fotos
CARPETA_FOTOS = 'uploads'
app.config['UPLOAD_FOLDER'] = CARPETA_FOTOS

# MAGIA: Crea la carpeta automáticamente si no existe
os.makedirs(CARPETA_FOTOS, exist_ok=True)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/subir', methods=['POST'])
def subir_datos():
    # 1. Capturamos el peso
    peso = request.form['peso']
    
    # 2. Capturamos la foto
    if 'foto' not in request.files:
        return "No enviaste foto."
    
    archivo_foto = request.files['foto']

    # 3. Guardamos la foto
    if archivo_foto.filename != '':
        nombre_seguro = secure_filename(archivo_foto.filename)
        ruta_final = os.path.join(app.config['UPLOAD_FOLDER'], nombre_seguro)
        
        archivo_foto.save(ruta_final)
        
        return f"<h1>¡Éxito!</h1><p>Peso: {peso}</p><p>Foto guardada en: {ruta_final}</p>"

    return "Error al guardar."

if __name__ == '__main__':
    app.run(debug=True)
