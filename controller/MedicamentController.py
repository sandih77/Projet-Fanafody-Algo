from model.MedicamentModel import MedicamentModel

class MedicamentController:
    @staticmethod
    def get_all_medicaments():
        medicaments = MedicamentModel.get_all_medicaments()
        return medicaments

    @staticmethod
    def add_medicament(nom, prix):
        MedicamentModel.add_medicament(nom, prix)

    @staticmethod
    def update_medicament(medicament_id, nom, prix):
        MedicamentModel.update_medicament(medicament_id, nom, prix)

    @staticmethod
    def delete_medicament(medicament_id):
        MedicamentModel.delete_medicament(medicament_id)