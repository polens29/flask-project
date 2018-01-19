from database import db


class Event(db.Model):
	id = db.Column('event_id', db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	description = db.Column(db.String(50))
	location = db.Column(db.String(200))
	type = db.Column(db.String(10))
	datetime = db.Column(db.DateTime)
