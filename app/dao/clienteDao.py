from flask import session
from app import app, db
from app.models.cliente import Cliente
from app.controllers.defaultController import index
from sqlalchemy import update

def obtener_clientes():
    clientes = Cliente.query.all()
    return clientes

def agrega_cliente(nombre, cedula, telefono, edad, sexo, id_cob):
    cliente = Cliente(nombre=nombre, cedula=cedula, telefono=telefono, edad=edad, sexo=sexo, id_cob=id_cob)
    db.session.add(cliente)
    db.session.commit()
    print(f"Cliente {nombre} agregado correctamente.")

def actualiza_cliente(nombre, cedula, telefono, edad, sexo, id_cob, id):
    cliente = Cliente.query.filter_by(id=id).first()
    cliente.nombre = nombre
    cliente.cedula = cedula
    cliente.telefono = telefono
    cliente.edad = edad
    cliente.sexo = sexo
    cliente.id_cob = id_cob
    db.session.commit()

def obtener_cliente_por_id(id):
    cliente = db.session.query(Cliente).get(id)
    print(cliente)
    return cliente

def borra_cliente(id):
    cliente = Cliente.query.filter_by(id=id).first()
    db.session.delete(cliente)
    db.session.commit()
    clientes = Cliente.query.all()
    return clientes
