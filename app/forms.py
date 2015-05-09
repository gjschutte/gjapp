from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class SpreukForm(Form):
	body = TextAreaField('body', validators=[Length(min=0, max=140)])
	auteur = StringField('auteur')
