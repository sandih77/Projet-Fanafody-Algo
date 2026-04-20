from flask import Blueprint, render_template, request

from controller.MedicamentController import MedicamentController
from controller.OrdonnanceController import OrdonnanceController
from controller.PrescriptionController import PrescriptionController
from .utils import safe_int


ordonnance_bp = Blueprint("ordonnance", __name__)


class OrdonnanceRoutes:
    @staticmethod
    def form_page():
        prescriptions = PrescriptionController.get_all_prescriptions()
        medicaments = MedicamentController.get_all_medicaments()
        return render_template(
            "pages/ordonnance_form.html",
            prescriptions=prescriptions,
            medicaments=medicaments,
            selected_prescription_id=None,
            selected_excluded_medicament_1_id=None,
            selected_excluded_medicament_2_id=None,
            active_page="ordonnance",
        )

    @staticmethod
    def evaluate():
        prescription_id = safe_int(request.form.get("prescription_id"))
        excluded_medicament_1_id = safe_int(request.form.get("excluded_medicament_1_id"))
        excluded_medicament_2_id = safe_int(request.form.get("excluded_medicament_2_id"))
        prescriptions = PrescriptionController.get_all_prescriptions()
        medicaments = MedicamentController.get_all_medicaments()

        if prescription_id is None:
            return render_template(
                "pages/ordonnance_form.html",
                prescriptions=prescriptions,
                medicaments=medicaments,
                selected_prescription_id=prescription_id,
                selected_excluded_medicament_1_id=excluded_medicament_1_id,
                selected_excluded_medicament_2_id=excluded_medicament_2_id,
                active_page="ordonnance",
                error="Veuillez selectionner une prescription.",
            )

        if (
            excluded_medicament_1_id is not None
            and excluded_medicament_2_id is not None
            and excluded_medicament_1_id == excluded_medicament_2_id
        ):
            return render_template(
                "pages/ordonnance_form.html",
                prescriptions=prescriptions,
                medicaments=medicaments,
                selected_prescription_id=prescription_id,
                selected_excluded_medicament_1_id=excluded_medicament_1_id,
                selected_excluded_medicament_2_id=excluded_medicament_2_id,
                active_page="ordonnance",
                error="Veuillez choisir deux medicaments differents pour la contrainte.",
            )

        excluded_pair = None
        if excluded_medicament_1_id is not None and excluded_medicament_2_id is not None:
            excluded_pair = (excluded_medicament_1_id, excluded_medicament_2_id)

        result = OrdonnanceController.solve_recursive_from_prescription(
            prescription_id,
            excluded_pair=excluded_pair,
        )

        if result["error"]:
            return render_template(
                "pages/ordonnance_form.html",
                prescriptions=prescriptions,
                medicaments=medicaments,
                selected_prescription_id=prescription_id,
                selected_excluded_medicament_1_id=excluded_medicament_1_id,
                selected_excluded_medicament_2_id=excluded_medicament_2_id,
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
