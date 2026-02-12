from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RegistrarArtigo(FlaskForm):
    titulo = StringField('Título do artigo', validators=[DataRequired()])
    conteudo = TextAreaField('Conteudo do artigo', validators=[DataRequired()])
    enviar = SubmitField('Publicar')