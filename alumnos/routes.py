from alumnos import alumnos
from flask import render_template, request, redirect, url_for
import forms
from models import db, Alumnos

@alumnos.route("/alumnos", methods=['GET','POST'])
def listado():
    create_form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    return render_template(
        "alumnos/listado_alumnos.html",
        form=create_form,
        alumno=alumno
    )

@alumnos.route("/agregarAlumnos", methods=['GET', 'POST'])
def agregar():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.listado'))
    return render_template("alumnos/agregar_alumnos.html", form=create_form)

@alumnos.route("/detallesAlumnos", methods=["GET"])
def detalles():
    id = request.args.get('id')
    alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    return render_template("alumnos/detalles_alumnos.html", alumno=alumno)

@alumnos.route("/modificarAlumnos", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono
    if request.method == 'POST':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.nombre = create_form.nombre.data
        alum1.apellidos = create_form.apellidos.data
        alum1.email = create_form.email.data
        alum1.telefono = create_form.telefono.data
        db.session.commit()
        return redirect(url_for('alumnos.listado'))
    return render_template("alumnos/modificar_alumnos.html", form=create_form)

@alumnos.route("/eliminarAlumnos", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono
    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.get(Alumnos, id)
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.listado'))
    return render_template("alumnos/eliminar_alumnos.html", form=create_form)