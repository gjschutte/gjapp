from flask import render_template, redirect, session, url_for, request
from app import app, db
from .forms import SpreukForm
from .models import Spreuk, Domein
import random
from ua_parser import user_agent_parser
from user_agents import parse

@app.route('/')
@app.route('/index')
def index():
	rand = random.randrange(0, Spreuk.query.count())
	spreuk = Spreuk.query[rand]
	
	return render_template('index.html',
							title='Home',
							spreuk=spreuk)

@app.route('/beheer', methods=['GET', 'POST'])
def beheer():
	form = SpreukForm()
	if form.validate_on_submit():
		d = Domein.query.get(2)
		spreuk = Spreuk(body=form.body.data, auteur=form.auteur.data, domain=form.soort.data)
		db.session.add(spreuk)
		db.session.commit()
		return redirect(url_for('beheer'))
	spreuken = Spreuk.query.all()
	return render_template('beheer.html', form=form, spreuken=spreuken)

@app.route('/analyse')
def analyse():
	# parse the user agent
	# user_agent_string = request.META.get('HTTP_USER_AGENT')
	user_agent_string = request.headers.get('User-Agent')
	user_agent = parse(user_agent_string)
	
	return render_template('analyse.html',
							title='Gegevens computer',
							user_agent = user_agent)
