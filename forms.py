from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app


def vaikas_query():
    return app.Vaikas.query


class TevasForm(FlaskForm):
    name = StringField("Number", [DataRequired()])
    surname = StringField("Surname", [DataRequired()])
    child = QuerySelectField(
        query_factory=vaikas_query,
        allow_blank=True,
        get_label="name",
        get_pk=lambda obj: str(obj),
    )
    submit = SubmitField("Submit")


class VaikasForm(FlaskForm):
    name = StringField("Number", [DataRequired()])
    surname = StringField("Surname", [DataRequired()])
    submit = SubmitField("Submit")
