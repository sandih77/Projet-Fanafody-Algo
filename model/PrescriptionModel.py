from database.db import mysql

class PrescriptionModel:
    @staticmethod
    def get_all_prescriptions():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM prescription ORDER BY id DESC")
        prescriptions = cursor.fetchall()
        cursor.close()
        return prescriptions

    @staticmethod
    def add_prescription(code_prescription, budget):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO prescription (code_prescription, budget) VALUES (%s, %s)",
            (code_prescription, budget),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_prescription(prescription_id, code_prescription, budget):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE prescription SET code_prescription = %s, budget = %s WHERE id = %s",
            (code_prescription, budget, prescription_id),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_prescription(prescription_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM prescription WHERE id = %s", (prescription_id,))
        mysql.connection.commit()
        cursor.close()