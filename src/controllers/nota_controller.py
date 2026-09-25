from flask import request, jsonify
from models.nota import Nota
from database import db

def listar_notas():
    notas = Nota.query.all()

    resultado = []

    for nota in notas:
        resultado.append({
            "id": nota.id,
            "estudiante": nota.estudiante,
            "asignatura": nota.asignatura,
            "periodo": nota.periodo,
            "calificacion": nota.calificacion
        })

    return jsonify(resultado)


def crear_nota():
    datos = request.get_json()

    nueva_nota = Nota(
        estudiante=datos["estudiante"],
        asignatura=datos["asignatura"],
        periodo=datos["periodo"],
        calificacion=datos["calificacion"]
    )

    db.session.add(nueva_nota)
    db.session.commit()

    return jsonify({"mensaje": "Nota creada correctamente"})