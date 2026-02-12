from app import db


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70))
    cedula = db.Column(db.Integer)
    telefono = db.Column(db.String(70))
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String(10))

    id_cob = db.Column(db.Integer, db.ForeignKey('coberturas.id'))
    cobertura = db.relationship('Cobertura', foreign_keys=id_cob)

    def __init__(self, nombre, cedula, telefono, edad, sexo, id_cob):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.edad = edad
        self.sexo = sexo
        self.id_cob = id_cob
