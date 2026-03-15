from flask import Blueprint, render_template, request, redirect, url_for

from controller.MedicamentController import MedicamentController
from controller.SymptomeController import SymptomeController
from controller.ParamMedicamentController import ParamMedicamentController
from .utils import safe_int, safe_float


param_medicament_bp = Blueprint("param_medicament", __name__)


class ParamMedicamentRoutes:
    @staticmethod
    def index():
        params = ParamMedicamentController.get_all_param_medicaments()
        medicaments = MedicamentController.get_all_medicaments()
        symptomes = SymptomeController.get_all_symptomes()
        return render_template(
            "pages/param_medicaments.html",
            param_medicaments=params,
            medicaments=medicaments,
            symptomes=symptomes,
            active_page="param_medicaments",
        )

    @staticmethod
    def add():
        medicament_id = safe_int(request.form.get("medicament_id"))
        symptome_id = safe_int(request.form.get("symptome_id"))
        efficacite = safe_float(request.form.get("efficacite"))

        if (
            medicament_id is not None
            and symptome_id is not None
            and efficacite is not None
            and 0 <= efficacite <= 100
        ):
            ParamMedicamentController.add_param_medicament(
                medicament_id,
                symptome_id,
                efficacite,
            )
        return redirect(url_for("param_medicament.index"))

    @staticmethod
    def update(param_id):
        medicament_id = safe_int(request.form.get("medicament_id"))
        symptome_id = safe_int(request.form.get("symptome_id"))
        efficacite = safe_float(request.form.get("efficacite"))

        if (
            medicament_id is not None
            and symptome_id is not None
            and efficacite is not None
            and 0 <= efficacite <= 100
        ):
            ParamMedicamentController.update_param_medicament(
                param_id,
                medicament_id,
                symptome_id,
                efficacite,
            )
        return redirect(url_for("param_medicament.index"))

    @staticmethod
    def delete(param_id):
        ParamMedicamentController.delete_param_medicament(param_id)
        return redirect(url_for("param_medicament.index"))


@param_medicament_bp.route("/param-medicaments")
def index():
    return ParamMedicamentRoutes.index()


@param_medicament_bp.route("/param-medicaments/add", methods=["POST"])
def add_param_medicament():
    return ParamMedicamentRoutes.add()


@param_medicament_bp.route("/param-medicaments/update/<int:param_id>", methods=["POST"])
def update_param_medicament(param_id):
    return ParamMedicamentRoutes.update(param_id)


@param_medicament_bp.route("/param-medicaments/delete/<int:param_id>", methods=["POST"])
def delete_param_medicament(param_id):
    return ParamMedicamentRoutes.delete(param_id)
