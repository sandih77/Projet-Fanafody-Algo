from database.db import mysql

class MedicamentModel:
    @staticmethod
    def get_all_medicaments():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM medicamemt")
        medicaments = cursor.fetchall()
        cursor.close()
        return medicaments
