from flask import Blueprint
from controllers.nota_controller import (
    listar_notas,
    crear_nota,
    actualizar_nota,
    eliminar_nota
)

nota_bp = Blueprint("nota_bp", __name__)

@nota_bp.route("/notas", methods=["GET"])
def notas():
    return listar_notas()

@nota_bp.route("/notas", methods=["POST"])
def guardar_nota():
    return crear_nota()

@nota_bp.route("/notas/<int:id>", methods=["PUT"])
def editar_nota(id):
    return actualizar_nota(id)

@nota_bp.route("/notas/<int:id>", methods=["DELETE"])
def borrar_nota(id):
    return eliminar_nota(id)