from database.db import mysql

class MedicamentModel:
    @staticmethod
    def get_all_medicaments():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medicament ORDER BY id DESC")
        medicaments = cursor.fetchall()
        cursor.close()
        return medicaments

    @staticmethod
    def add_medicament(nom, prix):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO medicament (nom, prix) VALUES (%s, %s)", (nom, prix))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_medicament(medicament_id, nom, prix):
        cursor = mysql.connection.cursor()
        cursor.execute(
            "UPDATE medicament SET nom = %s, prix = %s WHERE id = %s",
            (nom, prix, medicament_id),
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_medicament(medicament_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM medicament WHERE id = %s", (medicament_id,))
        mysql.connection.commit()
        cursor.close()
