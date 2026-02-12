from app import app
from flask import render_template, url_for, request, redirect
from app.dao import medicoDao, especialidadDao
def obtener_especialidades():
    especialidades = especialidadDao.obtener_especialidad()
    return especialidades

@app.route('/lista_medicos')
def leer_medico():
    medicos = medicoDao.obtener_medicos()
    especialidades = obtener_especialidades()
    return render_template('medicos.html', med=medicos, esp=especialidades)

@app.route("/add_medico", methods=['GET', 'POST'])
def add_medico():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        id_esp = int(request.form.get('id_esp'))
        medicoDao.agrega_medico(nombre, apellido, telefono, id_esp)
        print("Médico agregado. Redirigiendo a /lista_medicos...")
    return redirect(url_for('leer_medico'))

@app.route("/edit_medico", methods=['GET', 'POST'])
def edit_medico():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        id_esp = request.form.get('id_esp')
        id = request.form.get('id')
        medicoDao.actualiza_medico(nombre, apellido, telefono, id_esp, id)
    return redirect(url_for('leer_medico'))

@app.route('/obtener_medico/<int:id>')
def obtener_medico(id):
    medico = medicoDao.obtener_medico_por_id(id)
    print(medico)
    return render_template("medicos.html", med=medico)

@app.route("/delete_medico/<int:id>", methods=['GET', 'POST'])
def delete_medico(id):
    medicoDao.borra_medico(id)
    return redirect(url_for('leer_medico'))
