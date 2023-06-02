
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()




class blog(db.Model):
    __tablename__: "blog"
    id = db.Column (db.Integer, primary_key=True)
    username = db.Column (db.String)
    titulo = db.Column (db.String)
    texto = db.Column (db.String)



def post(usuario):
    Query = db.session.query(blog).filter(blog.username == usuario).order_by(blog.texto.desc()).limit(3)
    query = Query.all()
    Post = []
    
    Last1 = {}
    Last2 = {}
    Last3 = {}

    for i in query:
        if len(Post) == 0:
            Last1["titulo"] = i.titulo
            Last1["texto"] = i.texto
            Post.append(Last1)
        elif len(Post) == 1:
            Last2["titulo"] = i.titulo
            Last2["texto"] = i.texto
            Post.append(Last2)
        elif len(Post) == 2:
            Last3["titulo"] = i.titulo
            Last3["texto"] = i.texto
            Post.append(Last3)
        
    
          

    return Post

def insert(title,text,usuario):
    nuevo = blog(titulo = title, texto = text, username = usuario)

    db.session.add(nuevo)
    db.session.commit()

    return nuevo


if __name__=="__main__":
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdatabase.db"

    db.init_app(app)
    app.app_context().push()

    db.create_all()