from flask import render_template, redirect, session, url_for
from app import app
from .models import Spreuk, Domein

@app.route('/')
@app.route('/index')
def index():
	spreuk = Spreuk.query.first()
	
	return render_template('index.html',
							title='Home',
							spreuk=spreuk)
