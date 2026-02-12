from flask import session
from app import app, db
from app.models.reserva import Reserva
from sqlalchemy import update

def obtener_reservas():
    reservas = Reserva.query.all()
    return reservas

def agregar_reserva(id_cli, fecha, id_esp):
    reserva = Reserva(id_cli=id_cli, fecha=fecha, id_esp=id_esp)
    db.session.add(reserva)
    db.session.commit()
    print(f"Reserva para el cliente {id_cli} agregada correctamente.")

def actualizar_reserva(id_cli, fecha, id_esp, id_reserva):
    reserva = Reserva.query.filter_by(id=id_reserva).first()
    reserva.id_cli = id_cli
    reserva.fecha = fecha
    reserva.id_esp = id_esp
    db.session.commit()

def obtener_reserva_por_id(id):
    reserva = db.session.query(Reserva).get(id)
    print(reserva)
    return reserva

def borrar_reserva(id):
    reserva = Reserva.query.filter_by(id=id).first()
    db.session.delete(reserva)
    db.session.commit()
    reservas = Reserva.query.all()
    return reservas
