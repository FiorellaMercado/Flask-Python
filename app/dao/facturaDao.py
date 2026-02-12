from app import db
from app.models.factura import Factura
from sqlalchemy import update

def obtener_facturas():
    facturas = Factura.query.all()
    return facturas

def agregar_factura(ruc, descripcion, id_cli, monto, fecha):
    factura = Factura(ruc=ruc, descripcion=descripcion, id_cli=id_cli, monto=monto, fecha=fecha)
    db.session.add(factura)
    db.session.commit()
    print(f"Factura para el cliente {id_cli} agregada correctamente.")

def actualizar_factura(ruc, descripcion, id_cli, monto, fecha, id_factura):
    factura = Factura.query.filter_by(id=id_factura).first()
    factura.ruc = ruc
    factura.descripcion = descripcion
    factura.id_cli = id_cli
    factura.monto = monto
    factura.fecha = fecha
    db.session.commit()

def obtener_factura_por_id(id):
    factura = db.session.query(Factura).get(id)
    print(factura)
    return factura

def borrar_factura(id):
    factura = Factura.query.filter_by(id=id).first()
    db.session.delete(factura)
    db.session.commit()
    facturas = Factura.query.all()
    return facturas
