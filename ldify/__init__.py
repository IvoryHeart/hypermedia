import sys, json
from flask.globals import current_app
from flask import make_response
import collections

JSONLDIFY_MIME_TYPE = 'application/ld+json'

def ld_response(data='', status=200, headers=None, context=None, apiDoc=None, contentType=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        if contentType is not None:
            headers['Content-Type'] = contentType
        else:
            headers['Content-Type'] = current_app.config['JSONLDIFY_MIME_TYPE']

    if isinstance(data, list):
        data, context = listToCollection(data, context)

    if apiDoc is not None:
        headers = append_header(headers, descriptor='Link', value = "<http://localhost:5000" + apiDoc + ">; rel=\"http://www.w3.org/ns/hydra/core#apiDocumentation\"" )

    if context is not None:
        headers = append_header(headers, descriptor='Link', value = "<http://localhost:5000" + context + ">; rel=\"http://www.w3.org/ns/json-ld#context\"")

    print (type(data), file=sys.stderr)
    return make_response(json.dumps(data), status, headers)

def listToCollection(data, context):
    obj = {}
    obj['@context'] = '/contexts/collection.jsonld'
    obj['@id'] = './'
    obj['@type'] = 'hydra:Collection'
    obj['members'] = data

    return obj, obj['@context']
    #return data, obj['@context']

def append_header(headers, descriptor, value):
    headers = headers or {}

    if descriptor is None:
        return headers

    if value is None:
        return headers

    if descriptor in headers and headers[descriptor] is not None:
        headers[descriptor] = headers[descriptor] + " , "
    else:
        headers[descriptor] = ""

    headers[descriptor] = headers[descriptor] + value

    return headers
