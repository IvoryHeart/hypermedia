from flask import Flask, send_from_directory
from flask_restful import Resource, abort, reqparse
import os, sys, json
from ldify import ld_response, JSONLDIFY_MIME_TYPE
from data import entryPoint


app = Flask(__name__, static_url_path='')

contextPath= "/contexts/entryPoint.jsonld"
apiDocumentation = "/contexts/vocab.jsonld"

# ContextsList
# shows a list of all contexts, and lets you POST to add new contexts
class EntryPoint(Resource):
	def get(self):		
		return ld_response(json.dumps(entryPoint), 200, context = contextPath, apiDoc=apiDocumentation)