from flask import Blueprint, render_template, request, redirect, url_for

from controller.SymptomeController import SymptomeController


symptome_bp = Blueprint("symptome", __name__)


class SymptomeRoutes:
    @staticmethod
    def index():
        symptomes = SymptomeController.get_all_symptomes()
        return render_template(
            "pages/symptomes.html",
            symptomes=symptomes,
            active_page="symptomes",
        )

    @staticmethod
    def add():
        nom = request.form.get("nom", "").strip()
        if nom:
            SymptomeController.add_symptome(nom)
        return redirect(url_for("symptome.index"))

    @staticmethod
    def update(symptome_id):
        nom = request.form.get("nom", "").strip()
        if nom:
            SymptomeController.update_symptome(symptome_id, nom)
        return redirect(url_for("symptome.index"))

    @staticmethod
    def delete(symptome_id):
        SymptomeController.delete_symptome(symptome_id)
        return redirect(url_for("symptome.index"))


@symptome_bp.route("/symptomes")
def index():
    return SymptomeRoutes.index()


@symptome_bp.route("/symptomes/add", methods=["POST"])
def add_symptome():
    return SymptomeRoutes.add()


@symptome_bp.route("/symptomes/update/<int:symptome_id>", methods=["POST"])
def update_symptome(symptome_id):
    return SymptomeRoutes.update(symptome_id)


@symptome_bp.route("/symptomes/delete/<int:symptome_id>", methods=["POST"])
def delete_symptome(symptome_id):
    return SymptomeRoutes.delete(symptome_id)
