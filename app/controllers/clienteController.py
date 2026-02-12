from app import app
from flask import render_template, url_for, request, redirect
from app.dao import clienteDao, coberturaDao

def obtener_coberturas():
    coberturas = coberturaDao.obtener_coberturas()
    return coberturas

@app.route('/lista_clientes')
def leer_cliente():
    clientes = clienteDao.obtener_clientes()
    coberturas = obtener_coberturas()
    return render_template('clientes.html', cli=clientes, cob=coberturas)

@app.route("/add_cliente", methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cedula = int(request.form.get('cedula'))
        telefono = request.form.get('telefono')
        edad = int(request.form.get('edad'))
        sexo = request.form.get('sexo')
        id_cob = int(request.form.get('id_cob'))
        clienteDao.agrega_cliente(nombre, cedula, telefono, edad, sexo, id_cob)
        print("Cliente agregado. Redirigiendo a /lista_clientes...")
    return redirect(url_for('leer_cliente'))

@app.route("/edit_cliente", methods=['GET', 'POST'])
def edit_cliente():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        cedula = int(request.form.get('cedula'))
        telefono = request.form.get('telefono')
        edad = int(request.form.get('edad'))
        sexo = request.form.get('sexo')
        id_cob = int(request.form.get('id_cob'))
        id = request.form.get('id')
        clienteDao.actualiza_cliente(nombre, cedula, telefono, edad, sexo, id_cob, id)
    return redirect(url_for('leer_cliente'))

@app.route('/obtener_cliente/<int:id>')
def obtener_cliente(id):
    cliente = clienteDao.obtener_cliente_por_id(id)
    print(cliente)
    return render_template("clientes.html", cli=cliente)

@app.route("/delete_cliente/<int:id>", methods=['GET', 'POST'])
def delete_cliente(id):
    clienteDao.borra_cliente(id)
    return redirect(url_for('leer_cliente'))
