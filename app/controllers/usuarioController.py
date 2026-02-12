# Importaciones necesarias
from flask import render_template, url_for, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.dao import usuarioDao
from app import app

# Rutas y funciones existentes

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        clave = request.form['clave']
        usuario = usuarioDao.obtener_usuario_por_login(login)

        if usuario and usuario.clave == clave:
            login_user(usuario)

            # Redirige al usuario a la página a la que intentaba acceder inicialmente
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))

    return render_template('login.html')

# Otras rutas y funciones existentes


from flask_login import login_required

# ...

@app.route('/credito')
@login_required
def nota_de_credito():
    # Tu lógica para la nota de crédito
    return render_template('credito.html')


@app.route('/lista_usuarios')
@login_required
def leer_usuario():
    pst = usuarioDao.obtener_usuario()
    return render_template('usuarios.html', usu=pst)

@app.route("/add_usuario", methods=['GET', 'POST'])
@login_required
def add_usuario():
    if request.method == 'POST':
        log = request.form.get('log')
        cla = request.form.get('clav')
        nom = request.form.get('nom')
        usuarioDao.agrega_usuario(log, cla, nom)
        print("Usuario agregado. Redirigiendo a /lista_usuarios...")
    return redirect(url_for('leer_usuario'))

@app.route("/edit_usuario", methods=['GET', 'POST'])
@login_required
def edit_usuario():
    if request.method == "POST":
        log = request.form.get('log')
        cla = request.form.get('clav')
        nom = request.form.get('nom')
        id = request.form.get('id')
        usuarioDao.actualiza_usuario(log, cla, nom, id)
    return redirect(url_for('leer_usuario'))

@app.route('/obtener_usuario/<int:id>')
@login_required
def obtener_usuario(id):
    usu = usuarioDao.obtener_por_id(id)
    print(usu[0])
    return render_template("usuarios.html", usu=usu[0])

@app.route("/delete_usuario/<int:id>", methods=['GET', 'POST'])
@login_required
def delete_usuario(id):
    usuarioDao.borra_usuario(id)
    return redirect(url_for('leer_usuario'))

# Rutas y funciones del sistema de login

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
