from flask import Blueprint, render_template, redirect, session, url_for
from app import db
from app.beheer.forms import SpreukForm
from app.models import Spreuk, Domein
from flask.ext import menu

mod = Blueprint(
			'beheer', 
			__name__, 
			template_folder='templates',
			url_prefix='/beheer')

@mod.route('/', methods=['GET', 'POST'])
@menu.register_menu(mod, '.beheer', 'Configuration', order=1)
def beheer():
	form = SpreukForm()
	if form.validate_on_submit():
		d = Domein.query.get(2)
		spreuk = Spreuk(body=form.body.data, auteur=form.auteur.data, domain=form.soort.data)
		db.session.add(spreuk)
		db.session.commit()
		return redirect(url_for('beheer.beheer'))
	spreuken = Spreuk.query.all()
	return render_template('beheer.html', form=form, spreuken=spreuken)

