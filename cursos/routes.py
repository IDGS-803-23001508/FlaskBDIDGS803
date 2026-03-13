from cursos import cursos
from flask import render_template, request, redirect, url_for
import forms
from models import db, Curso, Alumnos, Maestros

@cursos.route("/cursos", methods=["GET", "POST"])
def listado():
    lista = Curso.query.all()
    return render_template("cursos/listado_cursos.html", cursos=lista)

@cursos.route("/agregarCursos", methods=["GET", "POST"])
def agregar():
    create_form = forms.CursoForm(request.form)
    if request.method == "POST":
        maestro_id = request.form.get('maestro_id')
        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=int(maestro_id) if maestro_id else None
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.listado'))
    lista_maestros = Maestros.query.all()
    return render_template("cursos/agregar_cursos.html", form=create_form, maestros=lista_maestros)

@cursos.route("/detallesCursos", methods=["GET"])
def detalles():
    id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == id).first()
    return render_template("cursos/detalles_cursos.html", curso=curso)

@cursos.route("/modificarCursos", methods=["GET", "POST"])
def modificar():
    create_form = forms.CursoForm(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id
    if request.method == "POST":
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = int(request.form.get('maestro_id'))
        db.session.commit()
        return redirect(url_for('cursos.listado'))
    lista_maestros = Maestros.query.all()
    return render_template("cursos/modificar_cursos.html", form=create_form, maestros=lista_maestros)

@cursos.route("/eliminarCursos", methods=["GET", "POST"])
def eliminar():
    create_form = forms.CursoForm(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id
    if request.method == "POST":
        id = create_form.id.data
        curso = db.session.get(Curso, id)
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.listado'))
    lista_maestros = Maestros.query.all()
    return render_template("cursos/eliminar_cursos.html", form=create_form, maestros=lista_maestros)

@cursos.route("/inscribirCursos", methods=["GET", "POST"])
def inscribir():
    mensaje = None
    categoria = None
    if request.method == "POST":
        alumno_id = request.form.get('alumno_id')
        curso_id = request.form.get('curso_id')
        alumno = db.session.get(Alumnos, alumno_id)
        curso = db.session.get(Curso, curso_id)
        if alumno and curso:
            if alumno in curso.alumnos:
                mensaje = f"{alumno.nombre} {alumno.apellidos} ya está inscrito en este curso."
                categoria = 'danger'
            else:
                curso.alumnos.append(alumno)
                db.session.commit()
                mensaje = f"{alumno.nombre} {alumno.apellidos} inscrito correctamente."
                categoria = 'success'
        # render the form again with message instead of redirecting
        curso = Curso.query.get(curso_id)
        alumnos = Alumnos.query.all()
        return render_template("cursos/inscribir_cursos.html",
                curso=curso, alumnos=alumnos,
                mensaje=mensaje, categoria=categoria)
    curso_id = request.args.get('id')
    curso = Curso.query.get(curso_id)
    alumnos = Alumnos.query.all()
    return render_template("cursos/inscribir_cursos.html", curso=curso, alumnos=alumnos)

@cursos.route("/consultarCursosAlumno", methods=["GET"])
def consultarCursosAlumno():
    lista = Curso.query.all()
    curso_id = request.args.get('curso_id')
    buscar = request.args.get('buscar')
    alumnos_curso = []
    curso_seleccionado = None
    mensaje = None
    categoria = None
    if curso_id:
        curso_seleccionado = db.session.get(Curso, curso_id)
        if curso_seleccionado and buscar:
            alumnos_curso = curso_seleccionado.alumnos
            if not alumnos_curso:
                mensaje = "Este curso no tiene alumnos inscritos."
                categoria = 'danger'
    return render_template("cursos/consultar_cursos_alumno.html", cursos=lista, alumnos_curso=alumnos_curso, curso_seleccionado=curso_seleccionado, mensaje=mensaje, categoria=categoria)

@cursos.route("/consultarAlumnoCursos", methods=["GET"])
def consultarAlumnoCursos():
    alumnos = Alumnos.query.all()
    alumno_id = request.args.get('alumno_id')
    buscar = request.args.get('buscar')

    cursos_alumno = []
    alumno_seleccionado = None
    mensaje = None
    categoria = None

    if alumno_id:
        alumno_seleccionado = db.session.get(Alumnos, alumno_id)

        if alumno_seleccionado and buscar:
            cursos_alumno = alumno_seleccionado.cursos

            if not cursos_alumno:
                mensaje = "Este alumno no está inscrito en ningún curso."
                categoria = "danger"

    return render_template(
        "cursos/consultar_alumno_cursos.html",
        alumnos=alumnos,
        cursos_alumno=cursos_alumno,
        alumno_seleccionado=alumno_seleccionado,
        mensaje=mensaje,
        categoria=categoria
    )

