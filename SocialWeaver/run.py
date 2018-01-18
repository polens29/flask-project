#!flask/bin/python
from flask import Flask

from database import db
from views import EventAPIView

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SocialWeaver.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.add_url_rule('/api/events/', view_func=EventAPIView.as_view('events'))

db.init_app(app)

if __name__ == '__main__':
	app.run(debug=True)