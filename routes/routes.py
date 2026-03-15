from flask import Blueprint, render_template
from controller.MedicamentController import MedicamentController
routes = Blueprint("routes", __name__)

@routes.route("/medicaments")
def get_medicaments():
    list_medoc = MedicamentController.get_all_medicaments()
    return render_template("pages/medicaments.html", medicaments=list_medoc)

@routes.route("/")
def home():
    return render_template("pages/index.html")