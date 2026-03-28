from model.PrescriptionModel import PrescriptionModel

class PrescriptionController:
    @staticmethod
    def get_all_prescriptions():
        return PrescriptionModel.get_all_prescriptions()

    @staticmethod
    def get_prescription_by_id(prescription_id):
        return PrescriptionModel.get_prescription_by_id(prescription_id)

    @staticmethod
    def add_prescription(code_prescription, budget):
        PrescriptionModel.add_prescription(code_prescription, budget)

    @staticmethod
    def update_prescription(prescription_id, code_prescription, budget):
        PrescriptionModel.update_prescription(prescription_id, code_prescription, budget)

    @staticmethod
    def delete_prescription(prescription_id):
        PrescriptionModel.delete_prescription(prescription_id)