from flask_wtf import FlaskForm # type: ignore
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit_btn = SubmitField('Login')



class SignUpForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit_btn = SubmitField('Sign Up')

class PokemonForm(FlaskForm):
    pokemon_name_id = StringField('Pokemon Name(or ID): ', validators=[DataRequired()])
    submit_btn = SubmitField('Search')
    submit_btn = SubmitField('CATCH')