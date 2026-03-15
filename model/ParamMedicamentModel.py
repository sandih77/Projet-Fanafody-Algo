from database.db import mysql


class ParamMedicamentModel:
    @staticmethod
    def get_all_param_medicaments():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT
                pm.id,
                pm.medicament_id,
                m.nom AS medicament_nom,
                pm.symptome_id,
                s.nom AS symptome_nom,
                pm.efficacite
            FROM param_medicament pm
            INNER JOIN medicament m ON pm.medicament_id = m.id
            INNER JOIN symptome s ON pm.symptome_id = s.id
            ORDER BY pm.id DESC
            """
        )
        params = cursor.fetchall()
        cursor.close()
        return params

    @staticmethod
    def add_param_medicament(medicament_id, symptome_id, efficacite):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO param_medicament (medicament_id, symptome_id, efficacite)
            VALUES (%s, %s, %s)
            """,
            (medicament_id, symptome_id, efficacite),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_param_medicament(param_id, medicament_id, symptome_id, efficacite):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE param_medicament
            SET medicament_id = %s, symptome_id = %s, efficacite = %s
            WHERE id = %s
            """,
            (medicament_id, symptome_id, efficacite, param_id),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_param_medicament(param_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM param_medicament WHERE id = %s", (param_id,))
        mysql.connection.commit()
        cursor.close()
