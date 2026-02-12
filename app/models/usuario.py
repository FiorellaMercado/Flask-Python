from app import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(10), unique=True, nullable=False)
    clave = db.Column(db.String(10))
    nombre = db.Column(db.String(60))

    def __init__(self, login, clave, nombre):
        self.login = login
        self.clave = clave
        self.nombre = nombre
