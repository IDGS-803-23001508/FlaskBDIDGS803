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

    apaterno = StringField('apaterno',  [
        validators.DataRequired(message='El campo es requerido')
    ])

    email = EmailField('correo',  [
        validators.Email(message='Ingrese un correo valido')
    ])