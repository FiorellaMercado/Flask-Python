from app import db
from app.models.cobertura import Cobertura

def obtener_coberturas():
    coberturas = Cobertura.query.all()
    return coberturas

def agregar_cobertura(tipo):
    cobertura = Cobertura(tipo)
    db.session.add(cobertura)
    db.session.commit()
    print(f"Cobertura {tipo} agregada correctamente.")

def actualizar_cobertura(tipo, id):
    res = Cobertura.query.filter_by(id=id).first()
    res.tipo = tipo
    db.session.commit()
    print(f"Cobertura actualizada correctamente.")

def obtener_cobertura_por_id(id):
    cobertura = db.session.query(Cobertura).get(id)
    print(cobertura)
    return cobertura

def borrar_cobertura(id):
    res = Cobertura.query.filter_by(id=id).first()
    db.session.delete(res)
    db.session.commit()
    print(f"Cobertura con ID {id} borrada correctamente.")
