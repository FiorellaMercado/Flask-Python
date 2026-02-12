from app import db

class Cobertura(db.Model):
    __tablename__ = 'coberturas'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))

    def __init__(self, tipo):
        self.tipo = tipo
