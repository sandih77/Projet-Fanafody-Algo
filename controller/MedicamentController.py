from model.MedicamentModel import MedicamentModel
from flask import jsonify

class MedicamentController:
    @staticmethod
    def get_all_medicaments():
        medicaments = MedicamentModel.get_all_medicaments()
        return medicaments