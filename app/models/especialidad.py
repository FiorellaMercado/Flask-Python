from app import db
class Especialidad(db.Model):
    __tablename__= 'especialidades'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    def __init__(self,nombre):
        self.nombre = nombre
    def __repr__(self):
        return '<Especialidad %s>' %self.nombre