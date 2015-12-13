from flask import Blueprint, render_template, redirect, session, url_for, request
from app import db
from flask.ext import menu

mod = Blueprint(
	'games', 
	__name__, 
	template_folder='templates',
	url_prefix='/games')

mod2 = Blueprint(
	'mathtest',
	__name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/games/mathtest')

@mod.route('/')
@menu.register_menu(mod, '.games', 'Games', order=4)
def games():
	
	return render_template('games.html',
							title='Games - index')

@mod2.route('/', methods = ['GET', 'POST'])
def mathtest():

	return render_template('mathtest.html',
							title='Math test' )
