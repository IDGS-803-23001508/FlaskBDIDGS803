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