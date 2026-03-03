from flask import render_template, request, redirect, url_for
from . import maestros
import forms
from models import db, Maestros


@maestros.route("/maestros", methods=['GET','POST'])
def listado():
    create_form = forms.MaesForm(request.form)
    lista_maestros = Maestros.query.all()
    return render_template(
        "maestros/listadoMaes.html",
        form=create_form,
        maestros=lista_maestros
    )


@maestros.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    form = forms.MaesForm(request.form)

    if request.method == "POST":
        maestro = Maestros(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            email=form.email.data,
            especialidad=form.especialidad.data
        )
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/maestros.html", form=form)

@maestros.route("/modificar", methods=["GET", "POST"])
def modificar():
    form = forms.MaesForm(request.form)

    if request.method == "GET":
        matricula = request.args.get("matricula")
        maestro = Maestros.query.get(matricula)
        form.matricula.data = maestro.matricula
        form.nombre.data = maestro.nombre
        form.apellidos.data = maestro.apellidos
        form.email.data = maestro.email
        form.especialidad.data = maestro.especialidad

    if request.method == "POST":
        matricula = form.matricula.data
        maestro = Maestros.query.get(matricula)

        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.email = form.email.data
        maestro.especialidad = form.especialidad.data

        db.session.commit()
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/modificar_maestros.html", form=form)

@maestros.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    form = forms.MaesForm(request.form)

    if request.method == "GET":
        matricula = request.args.get("matricula")
        maestro = Maestros.query.get(matricula)

        form.matricula.data = maestro.matricula
        form.nombre.data = maestro.nombre
        form.apellidos.data = maestro.apellidos
        form.email.data = maestro.email
        form.especialidad.data = maestro.especialidad

    if request.method == "POST":
        matricula = request.args.get("matricula")
        maestro = Maestros.query.get(matricula)
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros.listado'))

    return render_template("maestros/eliminar_maestros.html", form=form)

@maestros.route("/detalles")
def detalles():
    matricula = request.args.get("matricula")
    maestro = Maestros.query.get(matricula)

    return render_template(
        "maestros/detalles_maestros.html",
        matricula=maestro.matricula,
        nombre=maestro.nombre,
        apellidos=maestro.apellidos,
        email=maestro.email,
        especialidad=maestro.especialidad
    )

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"