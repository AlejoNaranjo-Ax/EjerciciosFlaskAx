from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos actualizada según tu phpMyAdmin
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bibliotecawulisesharrynsonoreyn'
mysql = MySQL(app)

# Clave para flash()
app.secret_key = 'mysecretkey'


@app.route("/")
def inicio():
    return render_template("contraseña.html")


@app.route('/Login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    password = request.form['password']

    if usuario == 'admin' and password == '1234':
        return render_template("menu.html")
    else:
        flash('Contraseña incorrecta, vuelve a intentarlo')
        return render_template("contraseña.html")


@app.route("/Menuprincipal")
def Menuprincipal():
    return render_template("menu.html")


@app.route("/Empleados")
def Empleados():
    return render_template("empleados.html")


@app.route('/Libros')
def Libros():
    cur = mysql.connection.cursor()
    # Consulta a la tabla 'books'
    cur.execute('SELECT * FROM books')
    data = cur.fetchall()
    cur.close()
    return render_template('libros.html', libros=data)


@app.route('/Bienvenidos')
def Bienvenidos():
    return render_template('Bienvenidos.html')


@app.route('/Agregar_Libro', methods=['POST'])
def AgregarLibro():
    # Asegúrate de que las llaves dentro de request.form matching con el HTML
    titulo = request.form['titulo']
    autor = request.form['autor']
    edicion = request.form['edicion']
    anho = request.form['anho']
    editorial = request.form['editorial']
    nopaginas = request.form['nopaginas']

    cur = mysql.connection.cursor()
    # Inserción con los nombres de columna exactos de tu tabla (Title, Author, Edition, Year, Publisher, no_pages)
    cur.execute(
        'INSERT INTO books (Title, Author, Edition, Year, Publisher, no_pages) '
        'VALUES (%s, %s, %s, %s, %s, %s)',
        (titulo, autor, edicion, anho, editorial, nopaginas)
    )
    mysql.connection.commit()
    cur.close()
    flash('Libro agregado satisfactoriamente')
    return redirect(url_for('Libros'))


if __name__ == '__main__':
    app.run(port=3600, debug=True)