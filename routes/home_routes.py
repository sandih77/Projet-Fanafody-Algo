from flask import Blueprint, render_template

from controller.MedicamentController import MedicamentController
from controller.SymptomeController import SymptomeController
from controller.PrescriptionController import PrescriptionController
from controller.ParamMedicamentController import ParamMedicamentController
from controller.ParamPrescriptionController import ParamPrescriptionController


home_bp = Blueprint("home", __name__)


class HomeRoutes:
    @staticmethod
    def index():
        stats = {
            "medicaments": len(MedicamentController.get_all_medicaments()),
            "symptomes": len(SymptomeController.get_all_symptomes()),
            "prescriptions": len(PrescriptionController.get_all_prescriptions()),
            "param_medicaments": len(ParamMedicamentController.get_all_param_medicaments()),
            "param_prescriptions": len(ParamPrescriptionController.get_all_param_prescriptions()),
        }
        return render_template("pages/index.html", stats=stats, active_page="home")


@home_bp.route("/")
def index():
    return HomeRoutes.index()
