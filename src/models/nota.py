from database import db
from datetime import datetime

class Nota(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    estudiante = db.Column(db.String(100), nullable=False)
    asignatura = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(20), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)

    fecha = db.Column(
        db.DateTime,
        default=datetime.now
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )