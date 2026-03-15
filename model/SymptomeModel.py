from database.db import mysql

class SymptomeModel:
    @staticmethod
    def get_all_symptomes():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM symptome ORDER BY id DESC")
        symptomes = cursor.fetchall()
        cursor.close()
        return symptomes

    @staticmethod
    def add_symptome(nom):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO symptome (nom) VALUES (%s)", (nom,))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_symptome(symptome_id, nom):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE symptome SET nom = %s WHERE id = %s", (nom, symptome_id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_symptome(symptome_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM symptome WHERE id = %s", (symptome_id,))
        mysql.connection.commit()
        cursor.close()