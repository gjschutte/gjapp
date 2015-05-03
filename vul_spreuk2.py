from app import db, models

u = models.Domein.query.get(2)
s = models.Spreuk(body='Als je iets gedaan wilt krijgen, geef de klus dan aan iemand die het druk heeft.', 
				auteur='Scott Parker', domain=u)
db.session.add(s)
db.session.commit()

domeinen = models.Domein.query.all()

for a in domeinen:
	print (a.id, a.soort, a.omschrijving)
	print (a)
	
spr = models.Spreuk.query.all()

for s in spr:
	print (s.id, s.body, s.auteur, s.domain)
