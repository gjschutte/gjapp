from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required

class SearchForm(Form):
	SearchString = StringField('Search: ', validators=[Required ('Please enter your search criteria')])
	


