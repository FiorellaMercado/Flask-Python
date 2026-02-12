from app import app
from flask import render_template, url_for, request, redirect
from app.dao import coberturaDao  # Asegúrate de importar el módulo de coberturas

@app.route('/lista_coberturas')
def leer_coberturas():
    coberturas = coberturaDao.obtener_coberturas()
    return render_template('coberturas.html', coberturas=coberturas)

@app.route("/add_cobertura", methods=['POST'])
def add_cobertura():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        coberturaDao.agregar_cobertura(tipo)
        print("Cobertura agregada. Redirigiendo a /lista_coberturas...")
    return redirect(url_for('leer_coberturas'))

@app.route("/edit_cobertura", methods=['POST'])
def edit_cobertura():
    if request.method == "POST":
        tipo = request.form.get('tipo')
        id = request.form.get('id')
        coberturaDao.actualizar_cobertura(tipo, id)
    return redirect(url_for('leer_coberturas'))

@app.route('/obtener_cobertura/<int:id>')
def obtener_cobertura(id):
    cobertura = coberturaDao.obtener_cobertura_por_id(id)
    print(cobertura)
    return render_template("coberturas.html", cobertura=cobertura)

@app.route("/delete_cobertura/<int:id>", methods=['GET', 'POST'])
def delete_cobertura(id):
    coberturaDao.borrar_cobertura(id)
    return redirect(url_for('leer_coberturas'))
