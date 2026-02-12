from flask import (session)
from app import app, db
from app.models import especialidad
from sqlalchemy import update

def obtener_especialidad():
    espe = especialidad.Especialidad.query.all()
    return espe

def agrega_especialidad(des):
    espe = especialidad.Especialidad(des)
    db.session.add(espe)
    db.session.commit()

def actualiza_especialidad(nom, id):
    res = especialidad.Especialidad.query.filter_by(id=id).first()
    res.nombre = nom
    res.id = id
    db.session.commit()
    especialidad.Especialidad.query.all()
def obtener_por_id(id):
    #espe = db.especialidad.Especialidad.query.filter_by(id=id)
    espe = db.session.query(especialidad.Especialidad).get(id)
    #espe = db.session.execute(db.select(Especialidad)).one()
    #espe = db.session.query(especialidad.Especialidad).get(id)
    print(espe)
    return espe
def borra_especialidad(idp):
    res = especialidad.Especialidad.query.filter_by(id=idp).first()
    db.session.delete(res)
    db.session.commit()
    res = especialidad.Especialidad.query.all()