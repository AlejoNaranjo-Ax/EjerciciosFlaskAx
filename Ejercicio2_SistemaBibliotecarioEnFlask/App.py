from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bibliotecawulisesharrynsonoreyn'

# Opcional: Retorna las consultas como diccionarios
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'


@app.route('/')
def inicio():
    return render_template('contraseña.html')


@app.route('/Login', methods=['POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario == 'admin' and password == '1234':
            return render_template('menu.html')
        else:
            flash('Contraseña incorrecta, vuelve a intentarlo')
            return render_template('contraseña.html')


@app.route('/Menuprincipal')
def Menuprincipal():
    return render_template('menu.html')


@app.route('/Empleados')
def Empleados():
    return render_template('empleados.html')


# Consultar todos los libros
@app.route('/Libros')
def Libros():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books')
    data = cur.fetchall()
    cur.close()
    return render_template('libros.html', libros=data)


# Agregar libro
@app.route('/Agregar_Libro', methods=['POST'])
def Agregar_Libro():
    if request.method == 'POST':
        titulo = request.form.get('Title') or request.form.get('titulo')
        autor = request.form.get('Author') or request.form.get('autor')
        edicion = request.form.get('Edition') or request.form.get('edicion')
        año = request.form.get('Year') or request.form.get('año')
        editorial = request.form.get('Publisher') or request.form.get('editorial')
        nopaginas = request.form.get('no_pages') or request.form.get('nopaginas')

        cur = mysql.connection.cursor()
        cur.execute(
            '''
            INSERT INTO books (Title, Author, Edition, Year, Publisher, no_pages)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''',
            (titulo, autor, edicion, año, editorial, nopaginas),
        )
        mysql.connection.commit()
        cur.close()

        flash('Libro agregado satisfactoriamente')
        return redirect(url_for('Libros'))


# Formulario para modificar libro
@app.route('/ModificarLibro/<id>')
def ModificarLibro(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books WHERE id=%s', (id,))
    data = cur.fetchone()
    cur.close()
    return render_template('modificarLibros.html', libros=data)


# Actualizar libro
@app.route('/ActualizarLibro/<id>', methods=['POST'])
def ActualizarLibro(id):
    if request.method == 'POST':
        titulo = request.form.get('Title') or request.form.get('titulo')
        autor = request.form.get('Author') or request.form.get('autor')
        edicion = request.form.get('Edition') or request.form.get('edicion')
        año = request.form.get('Year') or request.form.get('año')
        editorial = request.form.get('Publisher') or request.form.get('editorial')
        nopaginas = request.form.get('no_pages') or request.form.get('nopaginas')

        cur = mysql.connection.cursor()
        cur.execute(
            '''
            UPDATE books
            SET Title=%s,
                Author=%s,
                Edition=%s,
                Year=%s,
                Publisher=%s,
                no_pages=%s
            WHERE id=%s
        ''',
            (titulo, autor, edicion, año, editorial, nopaginas, id),
        )
        mysql.connection.commit()
        cur.close()

        flash('Libro actualizado exitosamente')
        return redirect(url_for('Libros'))


# Eliminar libro
@app.route('/EliminarLibro/<string:id>')
def EliminarLibro(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM books WHERE id=%s', (id,))
    mysql.connection.commit()
    cur.close()

    flash('Libro eliminado satisfactoriamente')
    return redirect(url_for('Libros'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)