#import flask
from flask import Flask
app = Flask(__name__)

# import blueprints
from api.redflags.endpoints import redendpoint

# register blueprints to the app
app.register_blueprint(redflags.endpoints.redendpoint, url_prefix='/api/v1')
