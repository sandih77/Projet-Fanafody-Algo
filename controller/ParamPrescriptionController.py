from model.ParamPrescriptionModel import ParamPrescriptionModel


class ParamPrescriptionController:
    @staticmethod
    def get_all_param_prescriptions():
        return ParamPrescriptionModel.get_all_param_prescriptions()

    @staticmethod
    def add_param_prescription(prescription_id, symptome_id, gravite):
        ParamPrescriptionModel.add_param_prescription(prescription_id, symptome_id, gravite)

    @staticmethod
    def update_param_prescription(param_id, prescription_id, symptome_id, gravite):
        ParamPrescriptionModel.update_param_prescription(param_id, prescription_id, symptome_id, gravite)

    @staticmethod
    def delete_param_prescription(param_id):
        ParamPrescriptionModel.delete_param_prescription(param_id)
