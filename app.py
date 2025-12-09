from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta 1: Muestra el formulario al entrar
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta 2: Recibe los datos cuando le das al botón "Guardar"
@app.route('/subir', methods=['POST'])
def subir_datos():
    # Aquí es donde capturaremos el peso y la foto más adelante
    return "<h1>¡Recibido!</h1><p>El sistema ha detectado el envío. (Pronto guardaremos la foto aquí).</p>"

if __name__ == '__main__':
    app.run(debug=True)
