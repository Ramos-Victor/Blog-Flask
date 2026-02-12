from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrarArtigo

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345'
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

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    artigos = Artigos.query.all()

    return render_template('index.html',
                            titulo = 'Index',
                            brand_name= 'Victor Blog',
                            now_year= datetime.now().year,
                            artigos=artigos)

@app.route('/admin_dashboard')
def admin_dashboard():
    artigos = Artigos.query.all()
    return render_template('admin/dashboard.html',
                            titulo = 'DashBoard',
                            brand_name= 'Victor Blog',
                            now_year= datetime.now().year,
                            artigos=artigos)

@app.route('/novo_artigo', methods=['GET','POST'])
def novo_artigo():
    form = RegistrarArtigo()
    if form.validate_on_submit():
        novo = Artigos(
            titulo=form.titulo.data,
            conteudo=form.conteudo.data,
            publicado_em=datetime.now()
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    
    return render_template(
        'admin/new.html',
        titulo='NovoArtigo',
        brand_name='Victor Blog',
        now_year=datetime.now().year,
        form=form
    )

@app.route('/artigo/<int:artigo_id>')
def artigo(artigo_id):
    artigo = Artigos.query.get(artigo_id)
    if artigo:
        return render_template('artigo.html', titulo = 'Artigo', brand_name= 'Victor Blog', now_year= datetime.now().year, artigo = artigo)
    
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('error/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)