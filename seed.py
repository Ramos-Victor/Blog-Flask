from app import db
from app import Artigos
from datetime import datetime

db.drop_all()
db.create_all()


for i in range (0,5):
    titulo = f'aaaaaa{i}'
    conteudo = f'bbb{i}'
    publicado_em = datetime.now()
    data = Artigos(titulo = titulo, conteudo = conteudo, publicado_em = publicado_em)
    db.session.add(data)

titulo = 'Minecraft melhor jogo da vida'
conteudo = 'Eu amo minecraft mais que tudo na vida amo jogar minecraft minecraft é daora pra krl'
publicado_em = datetime.now()
data = Artigos(titulo = titulo, conteudo = conteudo, publicado_em = publicado_em)
db.session.add(data)


db.session.commit()