from flask import Blueprint, render_template, redirect, session, url_for
from app import db
from app.models import Spreuk, Domein
import random
from flask.ext import menu

mod = Blueprint(
			'home', 
			__name__, 
			template_folder='templates')

@mod.route('/')
@menu.register_menu(mod, '/index', 'Home', order=0)
@mod.route('/index')
def index():
	rand = random.randrange(0, Spreuk.query.count())
	spreuk = Spreuk.query[rand]
	
	return render_template('index.html',
							title='Home',
							spreuk=spreuk)

