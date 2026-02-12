from flask import (session)
from app import app, db
from app.models.usuario import Usuario
from app.controllers.defaultController import index
from sqlalchemy import update
def obtener_usuario():
    usu = Usuario.query.all()
    return usu

def agrega_usuario(log,cla,nom):
    usu = Usuario(log,cla,nom)
    db.session.add(usu)
    db.session.commit()
    print(f"Usuario {nom} agregado correctamente.")
def actualiza_usuario(log,cla, nom, id):
    res = Usuario.query.filter_by(id=id).first()
    res.login = log
    res.clave = cla
    res.nombre = nom
    res.id = id
    db.session.commit()
    Usuario.query.all()
def obtener_por_id(id):
    # espe = usuario.usuario.query.filter_by(id=id)
    usu = db.session.query(Usuario).get(id)
    # espe = db.session.execute(db.select(usuario)).one()
    # espe = db.session.query(usuario.usuario).get(id)
    print(usu)
    return usu

def borra_usuario(idp):
    res = Usuario.query.filter_by(id=idp).first()
    db.session.delete(res)
    db.session.commit()
    res = Usuario.query.all()

def obtener_usuario_por_login(login):
    usuario = Usuario.query.filter_by(login=login).first()
    return usuario