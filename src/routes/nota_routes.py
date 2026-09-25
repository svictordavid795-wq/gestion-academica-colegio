from flask import Blueprint
from controllers.nota_controller import listar_notas

nota_bp = Blueprint("nota_bp", __name__)

@nota_bp.route("/notas")
def notas():
    return listar_notas()