# flask-project
Assignment from Social Weaver

# Events API

### Fields

name = CharField

description = CharField

location = CharField

type = CharField

datetime = DateTime



# API Endpoints

## Get all events

URL: /api/events/

METHOD: GET


## Get Specific event

URL: /api/events/?event_id=<event_id>

METHOD: GET

PARAMS: event_id


## Create New Event

URL: /api/events/

METHOD: POST

PARAMS: name, description, location, type, datetime


## Update Event

URL: /api/events/

METHOD: PUT

PARAMS: *updated fields*


## Delete Event

URL: /api/events/

METHOD: DELETE

PARAMS: event_id

