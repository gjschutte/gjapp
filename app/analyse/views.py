from flask import Blueprint, render_template, redirect, session, url_for, request
from app import db
from app.models import Spreuk, Domein
from ua_parser import user_agent_parser
from user_agents import parse
from flask.ext import menu

mod = Blueprint(
			'analyse', 
			__name__, 
			template_folder='templates',
			url_prefix='/analyse')

@mod.route('/')
@menu.register_menu(mod, '.analyse', 'Info computer', order=2)
def analyse():
	# parse the user agent
	# user_agent_string = request.META.get('HTTP_USER_AGENT')
	user_agent_string = request.headers.get('User-Agent')
	user_agent = parse(user_agent_string)
	
	return render_template('analyse.html',
							title='Gegevens computer',
							user_agent = user_agent)
