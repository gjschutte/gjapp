from app import db, models

d = models.Domein(soort='Spreuk', omschrijving ='Management')
db.session.add(d)
db.session.commit()
d = models.Domein(soort='Spreuk', omschrijving ='ICT')
db.session.add(d)
db.session.commit()
d = models.Domein(soort='Spreuk', omschrijving ='Humor')
db.session.add(d)
db.session.commit()
d = models.Domein(soort='Spreuk', omschrijving ='Overig')
db.session.add(d)
db.session.commit()


domeinen = models.Domein.query.all()

for a in domeinen:
	print (a.id, a.soort, a.omschrijving)
	print (a)
