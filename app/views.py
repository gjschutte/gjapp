from flask import render_template, redirect, session, url_for
from app import app, db
from .forms import SpreukForm
from .models import Spreuk, Domein

@app.route('/')
@app.route('/index')
def index():
	spreuk = Spreuk.query.first()
	
	return render_template('index.html',
							title='Home',
							spreuk=spreuk)

@app.route('/beheer', methods=['GET', 'POST'])
def beheer():
	form = SpreukForm()
	if form.validate_on_submit():
		d = Domein.query.get(2)
		spreuk = Spreuk(body=form.body.data, auteur=form.auteur.data, domain=d)
		db.session.add(spreuk)
		db.session.commit()
		return redirect(url_for('beheer'))
	spreuken = Spreuk.query.all()
	return render_template('beheer.html', form=form, spreuken=spreuken)
