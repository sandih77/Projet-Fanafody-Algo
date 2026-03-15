from model.SymptomeModel import SymptomeModel

class SymptomeController:
    @staticmethod
    def get_all_symptomes():
        return SymptomeModel.get_all_symptomes()

    @staticmethod
    def add_symptome(nom):
        SymptomeModel.add_symptome(nom)

    @staticmethod
    def update_symptome(symptome_id, nom):
        SymptomeModel.update_symptome(symptome_id, nom)

    @staticmethod
    def delete_symptome(symptome_id):
        SymptomeModel.delete_symptome(symptome_id)