from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Length

class PlaceForm(Form):
	City = StringField('City', validators=[Length(min=2, max=100)])
	


