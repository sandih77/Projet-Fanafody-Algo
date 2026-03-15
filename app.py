from flask import Flask
from config import Config
from database.db import mysql
from routes import register_blueprints

app = Flask(__name__)

app.config["MYSQL_HOST"] = Config.MYSQL_HOST
app.config["MYSQL_USER"] = Config.MYSQL_USER
app.config["MYSQL_PASSWORD"] = Config.MYSQL_PASSWORD
app.config["MYSQL_DB"] = Config.MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = Config.MYSQL_CURSORCLASS

mysql.init_app(app)

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)