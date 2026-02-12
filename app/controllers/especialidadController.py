from app import app
from flask import (render_template, url_for, request, redirect)
from app.dao import especialidadDao
@app.route('/lista_all')
def leer_especialidad():
    pst = especialidadDao.obtener_especialidad()
    return render_template('especialidad.html', esp=pst)
@app.route("/add_especialidad", methods=['GET','POST'])
def add_especialidad():
    if request.method == 'POST':
        des = request.form.get('desc')
        especialidadDao.agrega_especialidad(des)
    return redirect(url_for('leer_especialidad'))

@app.route("/edit_especialidad", methods=['GET','POST'])
def edit_especialidad():
    if request.method=="POST":
        desc = request.form.get('desc')
        id = request.form.get('id')
        especialidadDao.actualiza_especialidad(desc, id)
        return redirect(url_for('leer_especialidad'))

@app.route('/obtener_especialidad/<int:id>')
def obtener_especialidad(id):
    esp = especialidadDao.obtener_por_id(id)
    print(esp[0])
    return render_template("especialidad.html", esp=esp[0])

@app.route("/delete_especialidad/<int:id>", methods=['GET', 'POST'])
def delete_especilidad(id):
    especialidadDao.borra_especialidad(id)
    return redirect(url_for('leer_especialidad'))