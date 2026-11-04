from flask import Flask, render_template, request, redirect, url_for, flash
from proyecto import Proyecto
from base_datos import (
    crear_tabla,
    insertar_proyecto,
    obtener_proyectos,
    obtener_proyecto,
    actualizar_proyecto,
    eliminar_proyecto,
)

app = Flask(__name__)
app.secret_key = "clave_temporal_dia5"

crear_tabla()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        Nombre = request.form["Nombre"].strip()
        Fecha = request.form["Fecha"].strip()
        Hora = request.form["Hora"].strip()
        Lugar = request.form["Lugar"].strip()
        Responsable = request.form["Responsable"].strip()

        if not Nombre or not Fecha or not Hora or not Lugar or not Responsable:
            flash("Completa todos los campos.")
            return redirect(url_for("registrar"))

        nuevo_proyecto = Proyecto(
            Nombre,
            Fecha,
            Hora,
            Lugar,
            Responsable,
        )
        insertar_proyecto(nuevo_proyecto)
        flash("Proyecto registrado correctamente.")
        return redirect(url_for("ver_proyectos"))
    return render_template("registrar.html")

@app.route("/proyectos")
def ver_proyectos():
    proyectos = obtener_proyectos()
    return render_template("proyectos.html", proyectos=proyectos)

@app.route("/editar/<int:clave_del_programa>", methods=["GET", "POST"])
def editar_proyecto(clave_del_programa):
    proyecto = obtener_proyecto(clave_del_programa)
    if request.method == "POST":
        Nombre = request.form["Nombre"].strip()
        Fecha = request.form["Fecha"].strip()
        Hora = request.form["Hora"].strip()
        Lugar = request.form["Lugar"].strip()
        Responsable = request.form["Responsable"].strip()

        actualizar_proyecto(clave_del_programa, Nombre, Fecha, Hora, Lugar, Responsable)
        flash("Proyecto actualizado correctamente.")
        return redirect(url_for("ver_proyectos"))
    return render_template("editar.html", proyecto=proyecto)

@app.route("/eliminar/<int:clave_del_programa>", methods=["POST"])
def borrar_proyecto(clave_del_programa):
    eliminar_proyecto(clave_del_programa)
    flash("Proyecto eliminado correctamente.")
    return redirect(url_for("ver_proyectos"))

if __name__ == "__main__":
    app.run(debug=True)