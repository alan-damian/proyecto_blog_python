
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
    
    Last = {}

    for i in query:
       

        Last["titulo"] = i.titulo

        Last["texto"] = i.texto

        
    
          

        Post.append(Last)

    return Post


if __name__=="__main__":
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdatabase.db"

    db.init_app(app)
    app.app_context().push()

    db.create_all()