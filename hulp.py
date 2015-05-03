from app import db, models


spreuken = models.Spreuk.query.all()

for a in spreuken:
	print (a.id, a.body)
