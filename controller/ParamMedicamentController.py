from model.ParamMedicamentModel import ParamMedicamentModel


class ParamMedicamentController:
    @staticmethod
    def get_all_param_medicaments():
        return ParamMedicamentModel.get_all_param_medicaments()

    @staticmethod
    def add_param_medicament(medicament_id, symptome_id, efficacite):
        ParamMedicamentModel.add_param_medicament(medicament_id, symptome_id, efficacite)

    @staticmethod
    def update_param_medicament(param_id, medicament_id, symptome_id, efficacite):
        ParamMedicamentModel.update_param_medicament(param_id, medicament_id, symptome_id, efficacite)

    @staticmethod
    def delete_param_medicament(param_id):
        ParamMedicamentModel.delete_param_medicament(param_id)
