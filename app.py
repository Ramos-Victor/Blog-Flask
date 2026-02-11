from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artigos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Artigos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String, nullable = False)
    conteudo = db.Column(db.String, nullable = False)
    publicado_em = db.Column(db.Date, nullable = False)

def __repr__(self):
    return f'<Artigos {self.id}>'

db.create_all()

@app.route('/')
def index():
    artigos = Artigos.query.all()

    return render_template('index.html',
                            title = 'index',
                            brand_name= 'Toni Blog',
                            now_year= datetime.now().year,
                            artigos=artigos)

@app.route('/admin_dashboard')
def admin_dashboard():
    return 'hello'

@app.route('/artigo/<int:artigo_id>')
def artigo(artigo_id):
    artigo = artigo.get(artigo_id)
    if not artigo:
        return redirect(url_for('index'))
    return f'<h1>artigos</h1>'


if __name__ == '__main__':
    app.run(debug=True)