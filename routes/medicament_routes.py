from flask import Blueprint, render_template, request, redirect, url_for

from controller.MedicamentController import MedicamentController
from .utils import safe_float


medicament_bp = Blueprint("medicament", __name__)


class MedicamentRoutes:
    @staticmethod
    def index():
        medicaments = MedicamentController.get_all_medicaments()
        return render_template(
            "pages/medicaments.html",
            medicaments=medicaments,
            active_page="medicaments",
        )

    @staticmethod
    def add():
        nom = request.form.get("nom", "").strip()
        prix = safe_float(request.form.get("prix"))
        if nom and prix is not None and prix >= 0:
            MedicamentController.add_medicament(nom, prix)
        return redirect(url_for("medicament.index"))

    @staticmethod
    def update(medicament_id):
        nom = request.form.get("nom", "").strip()
        prix = safe_float(request.form.get("prix"))
        if nom and prix is not None and prix >= 0:
            MedicamentController.update_medicament(medicament_id, nom, prix)
        return redirect(url_for("medicament.index"))

    @staticmethod
    def delete(medicament_id):
        MedicamentController.delete_medicament(medicament_id)
        return redirect(url_for("medicament.index"))


@medicament_bp.route("/medicaments")
def index():
    return MedicamentRoutes.index()


@medicament_bp.route("/medicaments/add", methods=["POST"])
def add_medicament():
    return MedicamentRoutes.add()


@medicament_bp.route("/medicaments/update/<int:medicament_id>", methods=["POST"])
def update_medicament(medicament_id):
    return MedicamentRoutes.update(medicament_id)


@medicament_bp.route("/medicaments/delete/<int:medicament_id>", methods=["POST"])
def delete_medicament(medicament_id):
    return MedicamentRoutes.delete(medicament_id)
