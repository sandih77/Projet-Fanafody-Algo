from controller.MedicamentController import MedicamentController
from controller.ParamMedicamentController import ParamMedicamentController
from controller.ParamPrescriptionController import ParamPrescriptionController
from controller.PrescriptionController import PrescriptionController
from controller.SymptomeController import SymptomeController

from model.OrdonnanceModel import OrdonnanceModel


class OrdonnanceController:

    @staticmethod
    def solve(budget, symptome_gravites):
        medicaments = MedicamentController.get_all_medicaments()
        params = ParamMedicamentController.get_all_param_medicaments()
        symptomes = SymptomeController.get_all_symptomes()

        return OrdonnanceModel.solve(
            budget,
            symptome_gravites,
            medicaments,
            params,
            symptomes
        )

    @staticmethod
    def solve_recursive_from_prescription(prescription_id, excluded_pair=None):
        prescription = PrescriptionController.get_prescription_by_id(prescription_id)
        if not prescription:
            return {
                "error": "Prescription introuvable.",
            }

        param_prescriptions = ParamPrescriptionController.get_param_prescriptions_by_prescription_id(
            prescription_id
        )

        symptome_gravites = {}
        for row in param_prescriptions:
            gravite = float(row["gravite"])
            symptome_id = row["symptome_id"]
            symptome_gravites[symptome_id] = symptome_gravites.get(symptome_id, 0.0) + gravite

        medicaments = MedicamentController.get_all_medicaments()
        params = ParamMedicamentController.get_all_param_medicaments()
        symptomes = SymptomeController.get_all_symptomes()

        result = OrdonnanceModel.solve_recursive(
            float(prescription["budget"]),
            symptome_gravites,
            medicaments,
            params,
            symptomes,
            excluded_pair=excluded_pair,
        )
        result["prescription"] = prescription
        return result