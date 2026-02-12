from flask import session
from app import app, db
from app.models.medico import Medico
from app.controllers.defaultController import index
from sqlalchemy import update

def obtener_medicos():
    medicos = Medico.query.all()
    return medicos

def agrega_medico(nombre, apellido, telefono, id_esp):
    medico = Medico(nombre=nombre, apellido=apellido, telefono=telefono, id_esp=id_esp)
    db.session.add(medico)
    db.session.commit()
    print(f"Médico {nombre} agregado correctamente.")

def actualiza_medico(nombre, apellido, telefono, id_esp, id):
    medico = Medico.query.filter_by(id=id).first()
    medico.nombre = nombre
    medico.apellido = apellido
    medico.telefono = telefono
    medico.id_esp = id_esp
    db.session.commit()

def obtener_medico_por_id(id):
    medico = db.session.query(Medico).get(id)
    print(medico)
    return medico

def borra_medico(id):
    medico = Medico.query.filter_by(id=id).first()
    db.session.delete(medico)
    db.session.commit()
    medicos = Medico.query.all()
    return medicos