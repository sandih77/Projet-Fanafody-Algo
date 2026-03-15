from controller.MedicamentController import MedicamentController
from controller.ParamMedicamentController import ParamMedicamentController
from controller.SymptomeController import SymptomeController


class OrdonnanceController:
    @staticmethod
    def _prepare_candidates(symptome_gravites):
        medicaments = MedicamentController.get_all_medicaments()
        params = ParamMedicamentController.get_all_param_medicaments()

        symptomes_cibles = {}
        for symptome_id, gravite in symptome_gravites.items():
            if gravite > 0:
                symptomes_cibles[symptome_id] = gravite

        efficacite_par_medicament = {}
        for row in params:
            medicament_id = row["medicament_id"]
            symptome_id = row["symptome_id"]
            if symptome_id not in symptomes_cibles:
                continue

            # Efficacite stockee sur 0-100, convertie en impact sur echelle 0-10.
            reduction = float(row["efficacite"]) / 10.0

            if medicament_id not in efficacite_par_medicament:
                efficacite_par_medicament[medicament_id] = {}

            efficacite_par_medicament[medicament_id][symptome_id] = (
                efficacite_par_medicament[medicament_id].get(symptome_id, 0.0) + reduction
            )

        candidates = []
        for med in medicaments:
            med_id = med["id"]
            effets = efficacite_par_medicament.get(med_id, {})
            if not effets:
                continue

            candidates.append(
                {
                    "id": med_id,
                    "nom": med["nom"],
                    "prix": float(med["prix"]),
                    "effets": effets,
                }
            )

        # Trie simple pour proposer d'abord des ordonnances economiques.
        candidates = sorted(candidates, key=lambda item: item["prix"])
        return candidates, symptomes_cibles

    @staticmethod
    def _is_healed(symptomes_cibles, progress):
        for symptome_id, gravite in symptomes_cibles.items():
            if gravite - progress.get(symptome_id, 0.0) > 0:
                return False
        return True

    @staticmethod
    def _build_solution(selected, total_price, symptomes_cibles, progress, symptomes_labels):
        details = []
        for symptome_id, gravite in symptomes_cibles.items():
            reduction = progress.get(symptome_id, 0.0)
            reste = gravite - reduction
            details.append(
                {
                    "symptome_id": symptome_id,
                    "symptome_nom": symptomes_labels.get(symptome_id, f"Symptome {symptome_id}"),
                    "gravite_initiale": round(gravite, 2),
                    "reduction_totale": round(reduction, 2),
                    "reste": round(reste, 2),
                }
            )

        return {
            "medicaments": [item["nom"] for item in selected],
            "nombre_medicaments": len(selected),
            "total_prix": round(total_price, 2),
            "details_symptomes": details,
        }

    @staticmethod
    def solve_recursive(budget, symptome_gravites):
        candidates, symptomes_cibles = OrdonnanceController._prepare_candidates(symptome_gravites)
        symptomes = SymptomeController.get_all_symptomes()
        symptomes_labels = {row["id"]: row["nom"] for row in symptomes}

        if not symptomes_cibles:
            return {
                "symptomes_saisis": [],
                "ordonnances_budget": [],
                "ordonnance_moins_cher": None,
                "budget": round(budget, 2),
                "error": "Veuillez saisir au moins une gravite strictement positive.",
            }

        ordonnances_budget = []
        meilleure_globale = None

        symptomes_saisis = []
        for symptome_id, gravite in symptomes_cibles.items():
            symptomes_saisis.append(
                {
                    "id": symptome_id,
                    "nom": symptomes_labels.get(symptome_id, f"Symptome {symptome_id}"),
                    "gravite": round(gravite, 2),
                }
            )

        def recurse(index, selected, total_price, progress):
            nonlocal meilleure_globale

            if meilleure_globale is not None and total_price >= meilleure_globale["total_prix"]:
                return

            if index == len(candidates):
                if not selected:
                    return

                if OrdonnanceController._is_healed(symptomes_cibles, progress):
                    solution = OrdonnanceController._build_solution(
                        selected,
                        total_price,
                        symptomes_cibles,
                        progress,
                        symptomes_labels,
                    )

                    if total_price <= budget:
                        ordonnances_budget.append(solution)

                    if meilleure_globale is None or total_price < meilleure_globale["total_prix"]:
                        meilleure_globale = solution
                return

            recurse(index + 1, selected, total_price, progress)

            med = candidates[index]
            updated_progress = progress.copy()
            for symptome_id, reduction in med["effets"].items():
                updated_progress[symptome_id] = updated_progress.get(symptome_id, 0.0) + reduction

            recurse(
                index + 1,
                selected + [med],
                total_price + med["prix"],
                updated_progress,
            )

        progress_init = {}
        recurse(0, [], 0.0, progress_init)

        ordonnances_budget = sorted(ordonnances_budget, key=lambda row: row["total_prix"])

        return {
            "symptomes_saisis": symptomes_saisis,
            "ordonnances_budget": ordonnances_budget,
            "ordonnance_moins_cher": meilleure_globale,
            "budget": round(budget, 2),
            "error": None,
        }
