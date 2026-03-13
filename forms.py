from wtforms import Form 
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre',  [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message= 'Ingrese nombre valido')
    ])

    apellidos = StringField('apellidos',  [
        validators.DataRequired(message='El campo es requerido')
    ])

    email = EmailField('correo',  [
        validators.Email(message='Ingrese un correo valido')
    ])

    telefono = StringField('telefono',  [
        validators.DataRequired(message='El campo es requerido')
    ])

class MaesForm(Form):
    matricula = IntegerField('matricula')

    nombre = StringField('nombre',  [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=20, message='Ingrese un nombre válido')
    ])

    apellidos = StringField('apellidos',  [
        validators.DataRequired(message='El campo es requerido')
    ])

    email = EmailField('correo',  [
        validators.Email(message='Ingrese un correo válido')
    ])

    especialidad = StringField('especialidad',  [
        validators.DataRequired(message='El campo es requerido')
    ])

class CursoForm(Form):
    id = IntegerField('id', [validators.optional()])
    nombre = StringField("Nombre del Curso", [
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=1, max=150)
    ])
    descripcion = StringField("Descripción", [
        validators.DataRequired(message="La descripción es requerida")
    ])
    maestro_id = IntegerField("Matrícula del Maestro", [
        validators.optional()
    ])