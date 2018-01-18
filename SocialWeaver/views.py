from datetime import datetime

from flask import request, jsonify
from flask.views import MethodView
from models import Event
from database import db


class EventAPIView(MethodView):

	fields = ['id', 'name', 'description', 'type', 'datetime', 'location']

	def get_context_data(self, event):
		data = {}
		for field in self.fields:
			data[field] = getattr(event, field)

		return data

	def get(self):
		event_id = request.args.get('event_id', None)
		if event_id:
			event = Event.query.get_or_404(event_id)
			data = self.get_context_data(event)
		else:
			data = []
			for event in Event.query.all():
				data.append(self.get_context_data(event))

		return jsonify(data)

	def post(self):
		event = Event()
		for key, value in request.form.iteritems():
			if key == 'datetime' and value:
				value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

			setattr(event, key, value)

		db.session.add(event)
		db.session.commit()

		response = {
			'success': True,
			'data': self.get_context_data(event)
		}

		return jsonify(response)

	def put(self):
		event_id = request.form.get('event_id', None)
		event = Event.query.get_or_404(event_id)

		for key, value in request.form.iteritems():
			if key == 'datetime' and value:
				value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

			setattr(event, key, value)

		db.session.commit()

		response = {
			'success': True,
			'data': self.get_context_data(event)
		}

		return jsonify(response)

	def delete(self):
		event_id = request.form.get('event_id', None)
		event = Event.query.get_or_404(event_id)

		db.session.delete(event)

		return jsonify({
			'success': True
		})


