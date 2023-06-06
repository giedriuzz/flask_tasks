from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SqliteDatabase("db.db", Base)
db.create_detabase()
app = Flask(__name__)

db = SQLAlchemy(app)


class Tevas(db.Model):
    __tablename__ = "tevas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    vaikas_id = db.Column(db.Integer, db.ForeignKey("vaikas.id"))
    vaikas = db.relationship("Vaikas")


class Vaikas(db.Model):
    __tablename__ = "vaikas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)


if __name__ == "__main__":
    app.run(debug=True)
