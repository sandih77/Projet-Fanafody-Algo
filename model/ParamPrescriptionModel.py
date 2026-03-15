from database.db import mysql


class ParamPrescriptionModel:
    @staticmethod
    def get_all_param_prescriptions():
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT
                pp.id,
                pp.prescription_id,
                p.code_prescription,
                pp.symptome_id,
                s.nom AS symptome_nom,
                pp.gravite
            FROM param_prescription pp
            INNER JOIN prescription p ON pp.prescription_id = p.id
            INNER JOIN symptome s ON pp.symptome_id = s.id
            ORDER BY pp.id DESC
            """
        )
        params = cursor.fetchall()
        cursor.close()
        return params

    @staticmethod
    def add_param_prescription(prescription_id, symptome_id, gravite):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            INSERT INTO param_prescription (prescription_id, symptome_id, gravite)
            VALUES (%s, %s, %s)
            """,
            (prescription_id, symptome_id, gravite),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_param_prescription(param_id, prescription_id, symptome_id, gravite):
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            UPDATE param_prescription
            SET prescription_id = %s, symptome_id = %s, gravite = %s
            WHERE id = %s
            """,
            (prescription_id, symptome_id, gravite, param_id),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_param_prescription(param_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM param_prescription WHERE id = %s", (param_id,))
        mysql.connection.commit()
        cursor.close()
