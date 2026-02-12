# Importa db desde tu aplicación Flask
from app import db
from app.models.cliente import Cliente

class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True)
    ruc = db.Column(db.String(20))
    descripcion = db.Column(db.String(255))
    id_cli = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    monto = db.Column(db.Integer)
    fecha = db.Column(db.String(20))

    # Define la relación con la tabla externa
    cliente = db.relationship('Cliente', foreign_keys=id_cli)

    def __init__(self, ruc, descripcion, id_cli, monto, fecha):
        self.ruc = ruc
        self.descripcion = descripcion
        self.id_cli = id_cli
        self.monto = monto
        self.fecha = fecha
