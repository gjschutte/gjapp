from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required

class PlaceForm(Form):
	City = StringField('City', validators=[Required ('Please provide  a city')])
	


