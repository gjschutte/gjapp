from app import db

class Domein (db.Model):
	id = db.Column(db.Integer, primary_key=True)
	soort = db.Column(db.String(20), index=True)
	omschrijving = db.Column(db.String(20))
	spreuken = db.relationship('Spreuk', backref='domain', lazy='dynamic')
	
	def __repr__(self):
		return '<Domein %r>' % (self.omschrijving)

class Spreuk(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(250))
	auteur = db.Column(db.String(32))
	domein_id = db.Column(db.Integer, db.ForeignKey('domein.id'))
	
	def __repr__(self):
		return '<Spreuk %r>' % (self.body)

