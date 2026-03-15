from flask import Blueprint, render_template, request

from controller.OrdonnanceController import OrdonnanceController
from controller.SymptomeController import SymptomeController
from .utils import safe_float


ordonnance_bp = Blueprint("ordonnance", __name__)


class OrdonnanceRoutes:
    @staticmethod
    def form_page():
        symptomes = SymptomeController.get_all_symptomes()
        symptomes = sorted(symptomes, key=lambda row: row["nom"])
        return render_template(
            "pages/ordonnance_form.html",
            symptomes=symptomes,
            active_page="ordonnance",
        )

    @staticmethod
    def evaluate():
        budget = safe_float(request.form.get("budget"))
        if budget is None or budget < 0:
            symptomes = SymptomeController.get_all_symptomes()
            symptomes = sorted(symptomes, key=lambda row: row["nom"])
            return render_template(
                "pages/ordonnance_form.html",
                symptomes=symptomes,
                active_page="ordonnance",
                error="Budget invalide. Veuillez saisir une valeur positive.",
            )

        symptomes = SymptomeController.get_all_symptomes()
        symptome_gravites = {}
        for symptome in symptomes:
            key = f"gravite_{symptome['id']}"
            gravite = safe_float(request.form.get(key))
            if gravite is None:
                gravite = 0.0
            symptome_gravites[symptome["id"]] = gravite

        result = OrdonnanceController.solve_recursive(budget, symptome_gravites)

        if result["error"]:
            symptomes = sorted(symptomes, key=lambda row: row["nom"])
            return render_template(
                "pages/ordonnance_form.html",
                symptomes=symptomes,
                active_page="ordonnance",
                error=result["error"],
            )

        if result["ordonnances_budget"]:
            return render_template(
                "pages/ordonnance_resultats.html",
                active_page="ordonnance",
                result=result,
            )

        if result["ordonnance_moins_cher"] is not None:
            return render_template(
                "pages/ordonnance_moins_cher.html",
                active_page="ordonnance",
                result=result,
            )

        return render_template(
            "pages/ordonnance_resultats.html",
            active_page="ordonnance",
            result=result,
            warning="Aucune ordonnance ne permet de guerir avec les donnees actuelles.",
        )


@ordonnance_bp.route("/ordonnances")
def form_page():
    return OrdonnanceRoutes.form_page()


@ordonnance_bp.route("/ordonnances/evaluer", methods=["POST"])
def evaluate():
    return OrdonnanceRoutes.evaluate()
