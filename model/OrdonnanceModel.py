import math

class OrdonnanceModel:
    EPSILON = 1e-9

    @staticmethod
    def _prepare_candidates(medicaments, params, symptome_gravites):
        symptomes_cibles = {
            sid: float(gravite)
            for sid, gravite in symptome_gravites.items()
            if float(gravite) > 0
        }

        efficacite_par_medicament = {}

        for row in params:
            med_id = row["medicament_id"]
            symp_id = row["symptome_id"]

            if symp_id not in symptomes_cibles:
                continue

            reduction = float(row["efficacite"])
            if reduction <= 0:
                continue

            if med_id not in efficacite_par_medicament:
                efficacite_par_medicament[med_id] = {}

            efficacite_par_medicament[med_id][symp_id] = (
                efficacite_par_medicament[med_id].get(symp_id, 0.0) + reduction
            )

        candidates = []

        for med in medicaments:
            prix = float(med["prix"])
            if prix <= 0:
                continue

            effets = efficacite_par_medicament.get(med["id"], {})
            if not effets:
                continue

            max_use = 0
            for sid, gravite in symptomes_cibles.items():
                reduction = effets.get(sid, 0.0)
                if reduction > 0:
                    max_use = max(max_use, int(math.ceil(gravite / reduction)))

            if max_use <= 0:
                continue

            candidates.append(
                {
                    "id": med["id"],
                    "nom": med["nom"],
                    "prix": prix,
                    "effets": effets,
                    "max_use": max_use,
                }
            )

        return sorted(candidates, key=lambda x: x["prix"]), symptomes_cibles

    @staticmethod
    def _is_healed(symptomes_cibles, progress):
        for sid, gravite in symptomes_cibles.items():
            reste = gravite - progress.get(sid, 0.0)
            if reste > OrdonnanceModel.EPSILON:
                return False
        return True

    @staticmethod
    def _build_solution(counts, total_price, symptomes_cibles, progress, labels):
        items = []
        medicaments = []
        nombre_total = 0

        for entry in counts:
            if entry["quantite"] <= 0:
                continue

            items.append(
                {
                    "id": entry["id"],
                    "nom": entry["nom"],
                    "quantite": entry["quantite"],
                    "prix_unitaire": round(entry["prix"], 2),
                    "sous_total": round(entry["prix"] * entry["quantite"], 2),
                }
            )
            medicaments.append(f"{entry['nom']} x{entry['quantite']}")
            nombre_total += entry["quantite"]

        details_symptomes = []
        for sid, gravite in symptomes_cibles.items():
            reduction = progress.get(sid, 0.0)
            reste = gravite - reduction
            details_symptomes.append(
                {
                    "symptome_id": sid,
                    "symptome_nom": labels.get(sid, f"Symptome {sid}"),
                    "gravite_initiale": round(gravite, 2),
                    "reduction_totale": round(reduction, 2),
                    "reste": round(reste, 2),
                }
            )

        return {
            "items": items,
            "medicaments": medicaments,
            "nombre_medicaments": nombre_total,
            "total_prix": round(total_price, 2),
            "details_symptomes": details_symptomes,
        }

    @staticmethod
    def _format_result(budget, symptomes_cibles, labels, ordonnances_budget, meilleure_globale):
        return {
            "symptomes_saisis": [
                {
                    "id": sid,
                    "nom": labels.get(sid, f"Symptome {sid}"),
                    "gravite": round(g, 2),
                }
                for sid, g in symptomes_cibles.items()
            ],
            "ordonnances_budget": sorted(ordonnances_budget, key=lambda x: x["total_prix"]),
            "ordonnance_moins_cher": meilleure_globale,
            "budget": round(budget, 2),
            "error": None,
        }

    @staticmethod
    def solve_recursive(
        budget,
        symptome_gravites,
        medicaments,
        params,
        symptomes,
        index=0,
        candidates=None,
        symptomes_cibles=None,
        labels=None,
        total_price=0.0,
        progress=None,
        counts=None,
        ordonnances_budget=None,
        meilleure_globale=None,
        init=True,
    ):
        if init:
            candidates, symptomes_cibles = OrdonnanceModel._prepare_candidates(
                medicaments, params, symptome_gravites
            )
            labels = {s["id"]: s["nom"] for s in symptomes}

            if not symptomes_cibles:
                return {
                    "symptomes_saisis": [],
                    "ordonnances_budget": [],
                    "ordonnance_moins_cher": None,
                    "budget": round(budget, 2),
                    "error": "Aucun symptome avec gravite > 0 pour cette prescription.",
                }

            if not candidates:
                return {
                    "symptomes_saisis": [
                        {
                            "id": sid,
                            "nom": labels.get(sid, f"Symptome {sid}"),
                            "gravite": round(g, 2),
                        }
                        for sid, g in symptomes_cibles.items()
                    ],
                    "ordonnances_budget": [],
                    "ordonnance_moins_cher": None,
                    "budget": round(budget, 2),
                    "error": "Aucun medicament ne couvre les symptomes de cette prescription.",
                }

            progress = {}
            counts = []
            ordonnances_budget = []
            meilleure_globale = [None]

        if meilleure_globale[0] and total_price >= meilleure_globale[0]["total_prix"]:
            if init:
                return OrdonnanceModel._format_result(
                    budget, symptomes_cibles, labels, ordonnances_budget, meilleure_globale[0]
                )
            return

        if index == len(candidates):
            if counts and OrdonnanceModel._is_healed(symptomes_cibles, progress):
                solution = OrdonnanceModel._build_solution(
                    counts,
                    total_price,
                    symptomes_cibles,
                    progress,
                    labels,
                )

                if total_price <= budget + OrdonnanceModel.EPSILON:
                    ordonnances_budget.append(solution)

                if (
                    meilleure_globale[0] is None
                    or total_price < meilleure_globale[0]["total_prix"]
                ):
                    meilleure_globale[0] = solution

            if init:
                return OrdonnanceModel._format_result(
                    budget, symptomes_cibles, labels, ordonnances_budget, meilleure_globale[0]
                )
            return

        med = candidates[index]
        prix = med["prix"]
        max_count = med["max_use"]

        OrdonnanceModel.solve_recursive(
            budget,
            symptome_gravites,
            medicaments,
            params,
            symptomes,
            index=index + 1,
            candidates=candidates,
            symptomes_cibles=symptomes_cibles,
            labels=labels,
            total_price=total_price,
            progress=progress,
            counts=counts,
            ordonnances_budget=ordonnances_budget,
            meilleure_globale=meilleure_globale,
            init=False,
        )

        for qty in range(1, max_count + 1):
            new_total = total_price + (prix * qty)

            if meilleure_globale[0] and new_total >= meilleure_globale[0]["total_prix"]:
                break

            new_progress = progress.copy()
            for sid, reduction in med["effets"].items():
                new_progress[sid] = new_progress.get(sid, 0.0) + (reduction * qty)

            OrdonnanceModel.solve_recursive(
                budget,
                symptome_gravites,
                medicaments,
                params,
                symptomes,
                index=index + 1,
                candidates=candidates,
                symptomes_cibles=symptomes_cibles,
                labels=labels,
                total_price=new_total,
                progress=new_progress,
                counts=counts
                + [
                    {
                        "id": med["id"],
                        "nom": med["nom"],
                        "prix": prix,
                        "quantite": qty,
                    }
                ],
                ordonnances_budget=ordonnances_budget,
                meilleure_globale=meilleure_globale,
                init=False,
            )

        if init:
            return OrdonnanceModel._format_result(
                budget, symptomes_cibles, labels, ordonnances_budget, meilleure_globale[0]
            )

    @staticmethod
    def solve(budget, symptome_gravites, medicaments, params, symptomes):
        return OrdonnanceModel.solve_recursive(
            budget,
            symptome_gravites,
            medicaments,
            params,
            symptomes,
        )
