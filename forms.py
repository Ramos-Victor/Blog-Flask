from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegistrarArtigo(FlaskForm):
    titulo = StringField('titulo', validators=[DataRequired()])
    conteudo = StringField('titulo', validators=[DataRequired()])
    enviar = SubmitField('Submit')