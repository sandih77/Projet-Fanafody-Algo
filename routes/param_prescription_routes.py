from flask import Blueprint, render_template, request, redirect, url_for

from controller.PrescriptionController import PrescriptionController
from controller.SymptomeController import SymptomeController
from controller.ParamPrescriptionController import ParamPrescriptionController
from .utils import safe_int, safe_float


param_prescription_bp = Blueprint("param_prescription", __name__)


class ParamPrescriptionRoutes:
    @staticmethod
    def index():
        params = ParamPrescriptionController.get_all_param_prescriptions()
        prescriptions = PrescriptionController.get_all_prescriptions()
        symptomes = SymptomeController.get_all_symptomes()
        return render_template(
            "pages/param_prescriptions.html",
            param_prescriptions=params,
            prescriptions=prescriptions,
            symptomes=symptomes,
            active_page="param_prescriptions",
        )

    @staticmethod
    def add():
        prescription_id = safe_int(request.form.get("prescription_id"))
        symptome_id = safe_int(request.form.get("symptome_id"))
        gravite = safe_float(request.form.get("gravite"))

        if (
            prescription_id is not None
            and symptome_id is not None
            and gravite is not None
            and 0 <= gravite <= 10
        ):
            ParamPrescriptionController.add_param_prescription(
                prescription_id,
                symptome_id,
                gravite,
            )
        return redirect(url_for("param_prescription.index"))

    @staticmethod
    def update(param_id):
        prescription_id = safe_int(request.form.get("prescription_id"))
        symptome_id = safe_int(request.form.get("symptome_id"))
        gravite = safe_float(request.form.get("gravite"))

        if (
            prescription_id is not None
            and symptome_id is not None
            and gravite is not None
            and 0 <= gravite <= 10
        ):
            ParamPrescriptionController.update_param_prescription(
                param_id,
                prescription_id,
                symptome_id,
                gravite,
            )
        return redirect(url_for("param_prescription.index"))

    @staticmethod
    def delete(param_id):
        ParamPrescriptionController.delete_param_prescription(param_id)
        return redirect(url_for("param_prescription.index"))


@param_prescription_bp.route("/param-prescriptions")
def index():
    return ParamPrescriptionRoutes.index()


@param_prescription_bp.route("/param-prescriptions/add", methods=["POST"])
def add_param_prescription():
    return ParamPrescriptionRoutes.add()


@param_prescription_bp.route("/param-prescriptions/update/<int:param_id>", methods=["POST"])
def update_param_prescription(param_id):
    return ParamPrescriptionRoutes.update(param_id)


@param_prescription_bp.route("/param-prescriptions/delete/<int:param_id>", methods=["POST"])
def delete_param_prescription(param_id):
    return ParamPrescriptionRoutes.delete(param_id)
