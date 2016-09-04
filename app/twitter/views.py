from flask import Blueprint, render_template, redirect, session, url_for
from app import db
from app.beheer.forms import SpreukForm
from app.models import Spreuk, Domein
from flask.ext import menu
from .search_form import SearchForm
from .twitter import req_twitter

mod = Blueprint(
			'twitter', 
			__name__, 
			template_folder='templates',
			url_prefix='/twitter')

@mod.route('/', methods=['GET', 'POST'])
@menu.register_menu(mod, '.twitter', 'Twitter', order=5)
def twitter():

	# Form to ask for search criteria
	form = SearchForm ()

	if form.validate_on_submit():
		search_crit = form.SearchString.data
	else:
		search_crit = 'Apeldoorn'
	
	# get twitter info
	twitter_info = req_twitter(search_crit)

	return render_template('twitter.html',
							title='Twitter',
							form = form,
							twitter_info = twitter_info)
