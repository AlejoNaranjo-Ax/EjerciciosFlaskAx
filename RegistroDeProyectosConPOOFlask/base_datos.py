import pymysql

# Configura tus credenciales de MySQL (XAMPP/WAMP por defecto usan root sin contraseña)
def obtener_conexion():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='', 
        db='imcufidetvwulisesharrynsonoreyn',
        cursorclass=pymysql.cursors.DictCursor # Permite acceder a los datos por nombre de columna
    )

def crear_tabla():
    # Tu tabla ya existe en phpMyAdmin, pero puedes dejar esta función por si necesitas inicializar algo.
    pass

def insertar_proyecto(proyecto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        query = """
            INSERT INTO programasyproyectos (Nombre, Fecha, Hora, Lugar, Responsable) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (proyecto.Nombre, proyecto.Fecha, proyecto.Hora, proyecto.Lugar, proyecto.Responsable))
    conexion.commit()
    conexion.close()

def obtener_proyectos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM programasyproyectos")
        proyectos = cursor.fetchall()
    conexion.close()
    return proyectos

def obtener_proyecto(clave_del_programa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM programasyproyectos WHERE ClaveDelPrograma = %s", (clave_del_programa,))
        proyecto = cursor.fetchone()
    conexion.close()
    return proyecto

def actualizar_proyecto(clave_del_programa, nombre, fecha, hora, lugar, responsable):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        query = """
            UPDATE programasyproyectos 
            SET Nombre = %s, Fecha = %s, Hora = %s, Lugar = %s, Responsable = %s 
            WHERE ClaveDelPrograma = %s
        """
        cursor.execute(query, (nombre, fecha, hora, lugar, responsable, clave_del_programa))
    conexion.commit()
    conexion.close()

def eliminar_proyecto(clave_del_programa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM programasyproyectos WHERE ClaveDelPrograma = %s", (clave_del_programa,))
    conexion.commit()
    conexion.close()