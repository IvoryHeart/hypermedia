import sys
import json
from flask_restful import Resource, abort, reqparse
from flask import Flask, current_app

from ldify import ld_response, JSONLDIFY_MIME_TYPE
from data import books, authors


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('id')
parser.add_argument('description')

contextPath="/contexts/authors.jsonld"

apiDocumentation = "/contexts/vocab.jsonld#"

# BooksList
# shows a list of all books, and lets you POST to add new tasks
class AuthorList(Resource):
    def get(self):
        return ld_response(json.dumps(authors), 200, context=contextPath, apiDoc=apiDocumentation)

    def post(self):
        args = parser.parse_args()
        author_id = len(authors) + 1
        #book_id = 'books/%i' % todo_id
        author = {'id': author_id, 'name': args['name']}
        authors.append(author)
        #return author, 201
        return ld_response(json.dumps(author), 201, context=contextPath, apiDoc=apiDocumentation)

class Author(Resource):
    def get(self, author_id):
        author, index = abort_if_author_doesnt_exist(author_id)
            #return author, 200
        return ld_response(json.dumps(author), 200, context=contextPath, apiDoc=apiDocumentation)

    def delete(self, author_id):
    	author, index = abort_if_author_doesnt_exist(author_id)
    	#del authors[author_id]
    	authors.pop(index)
    	#return '', 204
    	return ld_response('', 204, context=contextPath, apiDoc=apiDocumentation)

    def post(self, author_id):
        args = parser.parse_args()
        #author, index = author_find(author_id)
        author, index = abort_if_author_doesnt_exist(author_id)
        #author = {'id': author_id, 'name': args['name']}
        print ("ARGS:: ", file=sys.stderr)
        print (args, file=sys.stderr)
        print ("AUTHOR:: ", file=sys.stderr)
        print ( author, file=sys.stderr)

        for key, value in args.items():
            if key in args and value is not None:
                author[key] = value

        authors[index] = author
        #return authors[author_id], 200
        return ld_response(json.dumps(author), 200, context=contextPath, apiDoc=apiDocumentation)

    def put(self, author_id):
        args = parser.parse_args()
    	#PUT is idempotent and it should take id in the request itself.
    	#author, index = author_find(author_id)
        author, index = abort_if_author_doesnt_exist(author_id)
        
        author = {'id': int(args['id']), 'name': args['name']}

        authors.append(author)
    	#return author, 201
        return ld_response(json.dumps(author), 200, context=contextPath, apiDoc=apiDocumentation)

def abort_if_author_doesnt_exist(author_id):
    author, index = author_find(author_id)
    if author is None:
        abort(404, message="Author {} doesn't exist".format(author_id))
        #ld_response("Author {} doesn't exist".format(author_id), status=404)
    else: 
        return author, index

def author_find(author_id):
    for index, author in enumerate(authors):
        print(author, file=sys.stderr)
        if author['id'] == int(author_id) or author['id'] == author_id:
            return author, index
    return None, -1