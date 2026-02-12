from app import db
class Medico(db.Model):
    __tablename__= 'medicos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70))
    apellido = db.Column(db.String(70))
    telefono = db.Column(db.String(70))

    id_esp = db.Column(db.Integer, db.ForeignKey('especialidades.id'))
    esp = db.relationship('Especialidad', foreign_keys=id_esp)

    def __init__(self, nombre, apellido, telefono,id_esp):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.id_esp = id_esp

