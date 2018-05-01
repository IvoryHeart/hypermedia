from flask import Flask, send_from_directory
from flask_restful import Resource, abort, reqparse
import os, sys, json
from ldify import ld_response, JSONLDIFY_MIME_TYPE


app = Flask(__name__, static_url_path='')

app.config['CONTEXTS_FOLDER'] = "../contexts/"

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('id')

# ContextsList
# shows a list of all contexts, and lets you POST to add new contexts
class Contexts(Resource):
	def get(self, contextName):		
		#TODO check context extension and load accordingly
		filePath = os.path.join(app.config['CONTEXTS_FOLDER'], contextName)

		with app.open_resource(filePath) as f:		
			#TODO: Check if file exists before reading.
			data = json.load(f)

		return ld_response(data, 200, context = "/contexts/" + contextName)