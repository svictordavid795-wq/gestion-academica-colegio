from flask import Flask
from database import db
from models.nota import Nota
from routes.nota_routes import nota_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gestion_academica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(nota_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return "Sistema de Gestion Academica"

if __name__ == "__main__":
    app.run(debug=True)