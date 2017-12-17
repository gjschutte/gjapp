from flask import Blueprint, render_template, redirect, session, url_for, request
from app import db
from flask.ext import menu

mod = Blueprint(
	'games', 
	__name__, 
	template_folder='templates',
	static_folder='static',
	url_prefix='/games')

mod2 = Blueprint(
	'mathtest',
	__name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/games/mathtest')

mod3 = Blueprint(
	'calculator',
	__name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/games/calculator')

mod4 = Blueprint(
	'simon',
	__name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/games/simon')

mod5 = Blueprint(
	'tictacto',
	__name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/games/tictacto')

mod6 = Blueprint(
	'pomodoro',
	__name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/games/pomodoro')

@mod.route('/')
@menu.register_menu(mod, '.games', 'Games', order=4)
def games():
	
	return render_template('games.html',
							title='Games - index')

@mod2.route('/', methods = ['GET', 'POST'])
def mathtest():

	return render_template('mathtest.html',
							title='Math test' )

@mod3.route('/')
def calculator():

	return render_template('calculator.html',
							title='Calculator' )

@mod4.route('/')
def simon():

	return render_template('simon.html',
							title='Simon' )

@mod5.route('/')
def tictacto():

	return render_template('tictacto.html',
							title='Tictacto' )

@mod6.route('/')
def pomodoro():

	return render_template('pomodoro.html',
							title='Pomodoro' )
