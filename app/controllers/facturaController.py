from app import app
from flask import render_template, url_for, request, redirect
from app.dao import facturaDao, clienteDao  # Asegúrate de importar los módulos necesarios

def obtener_clientes():
    clientes = clienteDao.obtener_clientes()
    return clientes

@app.route('/lista_facturas')
def leer_facturas():
    facturas = facturaDao.obtener_facturas()
    clientes = obtener_clientes()
    return render_template('facturas.html', facturas=facturas, clientes=clientes)

@app.route("/add_factura", methods=['GET', 'POST'])
def add_factura():
    if request.method == 'POST':
        ruc = request.form.get('ruc')
        descripcion = request.form.get('descripcion')
        id_cli = int(request.form.get('id_cli'))
        monto = int(request.form.get('monto'))
        fecha = request.form.get('fecha')
        facturaDao.agregar_factura(ruc, descripcion, id_cli, monto, fecha)
        print("Factura agregada. Redirigiendo a /lista_facturas...")
    return redirect(url_for('leer_facturas'))

@app.route("/edit_factura", methods=['GET', 'POST'])
def edit_factura():
    if request.method == "POST":
        ruc = request.form.get('ruc')
        descripcion = request.form.get('descripcion')
        id_cli = int(request.form.get('id_cli'))
        monto = int(request.form.get('monto'))
        fecha = request.form.get('fecha')
        id_factura = int(request.form.get('id_factura'))
        facturaDao.actualizar_factura(ruc, descripcion, id_cli, monto, fecha, id_factura)
    return redirect(url_for('leer_facturas'))

@app.route('/obtener_factura/<int:id>')
def obtener_factura(id):
    factura = facturaDao.obtener_factura_por_id(id)
    clientes = obtener_clientes()
    return render_template("facturas.html", factura=factura, clientes=clientes)

@app.route("/delete_factura/<int:id>", methods=['GET', 'POST'])
def delete_factura(id):
    facturaDao.borrar_factura(id)
    return redirect(url_for('leer_facturas'))
