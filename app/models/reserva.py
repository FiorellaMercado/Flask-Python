from app import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    id_cli = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha = db.Column(db.String(20))
    id_esp = db.Column(db.Integer, db.ForeignKey('especialidades.id'))

    # Define las relaciones con las tablas externas
    cliente = db.relationship('Cliente', foreign_keys=id_cli)
    especialidad = db.relationship('Especialidad', foreign_keys=id_esp)

    def __init__(self, id_cli, fecha, id_esp):
        self.id_cli = id_cli
        self.fecha = fecha
        self.id_esp = id_esp