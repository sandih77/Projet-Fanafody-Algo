from flask import Blueprint, render_template, request, redirect, url_for

from controller.PrescriptionController import PrescriptionController
from .utils import safe_float


prescription_bp = Blueprint("prescription", __name__)


class PrescriptionRoutes:
    @staticmethod
    def index():
        prescriptions = PrescriptionController.get_all_prescriptions()
        return render_template(
            "pages/prescriptions.html",
            prescriptions=prescriptions,
            active_page="prescriptions",
        )

    @staticmethod
    def add():
        code_prescription = request.form.get("code_prescription", "").strip()
        budget = safe_float(request.form.get("budget"))
        if code_prescription and budget is not None and budget >= 0:
            PrescriptionController.add_prescription(code_prescription, budget)
        return redirect(url_for("prescription.index"))

    @staticmethod
    def update(prescription_id):
        code_prescription = request.form.get("code_prescription", "").strip()
        budget = safe_float(request.form.get("budget"))
        if code_prescription and budget is not None and budget >= 0:
            PrescriptionController.update_prescription(
                prescription_id,
                code_prescription,
                budget,
            )
        return redirect(url_for("prescription.index"))

    @staticmethod
    def delete(prescription_id):
        PrescriptionController.delete_prescription(prescription_id)
        return redirect(url_for("prescription.index"))


@prescription_bp.route("/prescriptions")
def index():
    return PrescriptionRoutes.index()


@prescription_bp.route("/prescriptions/add", methods=["POST"])
def add_prescription():
    return PrescriptionRoutes.add()


@prescription_bp.route("/prescriptions/update/<int:prescription_id>", methods=["POST"])
def update_prescription(prescription_id):
    return PrescriptionRoutes.update(prescription_id)


@prescription_bp.route("/prescriptions/delete/<int:prescription_id>", methods=["POST"])
def delete_prescription(prescription_id):
    return PrescriptionRoutes.delete(prescription_id)
