from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.ext.sqlalchemy.orm import QuerySelectField
from wtforms.validators import Required, Length
from app.models import Domein


def domeinen():
    return Domein.query.filter_by(soort='Spreuk').order_by(Domein.omschrijving).all()


class SpreukForm(Form):
    body = TextAreaField('Quote', validators=[Length(min=1, max=250, message=
    (u'Quote should be filled and no longer than 250 characters'))])
    auteur = StringField('Author', validators=[Required('Please provide an author')])
    soort = QuerySelectField('Category', query_factory=domeinen, get_label="omschrijving", allow_blank=False)
