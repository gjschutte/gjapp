from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.ext.sqlalchemy.orm import QuerySelectField
from wtforms.validators import DataRequired, Length
from .models import Domein

def domeinen():
	return Domein.query.filter_by(soort='Spreuk').order_by(Domein.omschrijving).all()

class SpreukForm(Form):
	body = TextAreaField('body', validators=[Length(min=0, max=140)])
	auteur = StringField('auteur')
	
	soort = QuerySelectField('soort', query_factory=domeinen, get_label="omschrijving", allow_blank=False)

