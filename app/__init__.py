from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyectoClinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'micodigosecreto'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # 'login' es el nombre de tu ruta de inicio de sesión

from app.controllers import (defaultController, especialidadController,
                             usuarioController, medicoController, clienteController, reservaController, coberturaController, facturaController)
from app.dao import (especialidadDao,usuarioDao,medicoDao, clienteDao,  reservaDao, coberturaDao, facturaDao)
from app.models import (especialidad, medico,usuario, cliente, reserva, cobertura, factura)

with app.app_context():
    db.create_all()

