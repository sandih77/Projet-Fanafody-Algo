from flask import Blueprint, render_template, request

from controller.OrdonnanceController import OrdonnanceController
from controller.PrescriptionController import PrescriptionController
from .utils import safe_int


ordonnance_bp = Blueprint("ordonnance", __name__)


class OrdonnanceRoutes:
    @staticmethod
    def form_page():
        prescriptions = PrescriptionController.get_all_prescriptions()
        return render_template(
            "pages/ordonnance_form.html",
            prescriptions=prescriptions,
            active_page="ordonnance",
        )

    @staticmethod
    def evaluate():
        prescription_id = safe_int(request.form.get("prescription_id"))
        prescriptions = PrescriptionController.get_all_prescriptions()

        if prescription_id is None:
            return render_template(
                "pages/ordonnance_form.html",
                prescriptions=prescriptions,
                active_page="ordonnance",
                error="Veuillez selectionner une prescription.",
            )

        result = OrdonnanceController.solve_recursive_from_prescription(prescription_id)

        if result["error"]:
            return render_template(
                "pages/ordonnance_form.html",
                prescriptions=prescriptions,
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
