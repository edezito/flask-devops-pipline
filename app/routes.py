from flask import Blueprint, request, jsonify

bp = Blueprint('routes', __name__)

@bp.route("/")
def index():
    return {"message": "API está no ar!"}

@bp.route("/protegido")
def protegido():
    token = request.headers.get("Authorization")
    if token == "Bearer meu-token":
        return {"mensagem": "Acesso autorizado"}
    return {"erro": "Token inválido"}, 401
