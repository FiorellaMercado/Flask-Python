from app import app
from flask import render_template, url_for, request, redirect
from app.dao import reservaDao, clienteDao, especialidadDao  # Asegúrate de importar los módulos necesarios

def obtener_clientes():
    clientes = clienteDao.obtener_clientes()
    return clientes

def obtener_especialidades():
    especialidades = especialidadDao.obtener_especialidad()
    return especialidades

@app.route('/lista_reservas')
def leer_reservas():
    reservas = reservaDao.obtener_reservas()
    clientes = obtener_clientes()
    especialidades = obtener_especialidades()
    return render_template('reservas.html', reservas=reservas, clientes=clientes, especialidades=especialidades)

@app.route("/add_reserva", methods=['GET', 'POST'])
def add_reserva():
    if request.method == 'POST':
        id_cli = int(request.form.get('id_cli'))
        fecha = request.form.get('fecha')
        id_esp = int(request.form.get('id_esp'))
        reservaDao.agregar_reserva(id_cli, fecha, id_esp)
        print("Reserva agregada. Redirigiendo a /lista_reservas...")
    return redirect(url_for('leer_reservas'))

@app.route("/edit_reserva", methods=['GET', 'POST'])
def edit_reserva():
    if request.method == "POST":
        id_cli = int(request.form.get('id_cli'))
        fecha = request.form.get('fecha')
        id_esp = int(request.form.get('id_esp'))
        id_reserva = int(request.form.get('id_reserva'))
        reservaDao.actualizar_reserva(id_cli, fecha, id_esp, id_reserva)
    return redirect(url_for('leer_reservas'))

@app.route('/obtener_reserva/<int:id>')
def obtener_reserva(id):
    reserva = reservaDao.obtener_reserva_por_id(id)
    clientes = obtener_clientes()
    especialidades = obtener_especialidades()
    return render_template("reservas.html", reserva=reserva, clientes=clientes, especialidades=especialidades)

@app.route("/delete_reserva/<int:id>", methods=['GET', 'POST'])
def delete_reserva(id):
    reservaDao.borrar_reserva(id)
    return redirect(url_for('leer_reservas'))
