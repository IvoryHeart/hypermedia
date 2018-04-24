import sys, json
from flask.globals import current_app
from flask import make_response

JSONLDIFY_MIME_TYPE = 'application/ld+json'

def ld_response(data='', status=200, headers=None, context=None, apiDoc=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = current_app.config['JSONLDIFY_MIME_TYPE']

    if context is not None:
        headers = append_header(headers, descriptor='Link', value = "<http://localhost:5000" + context + ">; rel=\"http://www.w3.org/ns/json-ld#context\"")

    if apiDoc is not None:
        headers = append_header(headers, descriptor='Link', value = "<http://localhost:5000" + apiDoc + ">; rel=\"http://www.w3.org/ns/hydra/core#apiDocumentation\"" )

    return make_response(data, status, headers)


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
