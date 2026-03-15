from .home_routes import home_bp
from .medicament_routes import medicament_bp
from .symptome_routes import symptome_bp
from .prescription_routes import prescription_bp
from .param_medicament_routes import param_medicament_bp
from .param_prescription_routes import param_prescription_bp
from .ordonnance_routes import ordonnance_bp


ALL_BLUEPRINTS = (
	home_bp,
	medicament_bp,
	symptome_bp,
	prescription_bp,
	param_medicament_bp,
	param_prescription_bp,
	ordonnance_bp,
)


def register_blueprints(app):
	for blueprint in ALL_BLUEPRINTS:
		app.register_blueprint(blueprint)
