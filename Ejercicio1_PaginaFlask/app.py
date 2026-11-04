from flask import Flask, render_template, abort
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión a la base de datos creada en phpMyAdmin (ver ../biblioteca.sql)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bibliotecawulisesharrynsonoreyn'
mysql = MySQL(app)


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')


# Ruta que consulta todos los libros de la tabla "libros"
@app.route('/libros')
def libros():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books')
    data = cur.fetchall()
    cur.close()
    return render_template('libros.html', libros=data)


# Ruta con parámetro: detalle de un libro
@app.route('/libro/<int:id>')
def libro(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM books WHERE id=%s', (id,))
    data = cur.fetchone()
    cur.close()
    if data is None:
        abort(404)
    return render_template('detalle.html', libro=data)


if __name__ == '__main__':
    app.run(port=3000, debug=True) 
