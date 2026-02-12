from app import app, db
from flask_login import LoginManager, UserMixin, login_required
from flask_login import current_user
from flask import render_template
from flask_login import login_required
from flask import redirect, url_for

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Esta función carga el objeto de usuario basado en el user_id
    from app.models.usuario import Usuario  # Asegúrate de importar tu modelo Usuario correctamente
    return Usuario.query.get(int(user_id))

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('inicio'))

@app.route('/inicio')
@login_required
def inicio():
    # Lógica para la página de inicio
    return render_template("inicio.html")

if __name__ == '__main__':
    app.run()
