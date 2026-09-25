from flask import Blueprint
from controllers.nota_controller import listar_notas, crear_nota

nota_bp = Blueprint("nota_bp", __name__)

@nota_bp.route("/notas", methods=["GET"])
def notas():
    return listar_notas()


@nota_bp.route("/notas", methods=["POST"])
def guardar_nota():
    return crear_nota()