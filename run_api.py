from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from resources.Authors import AuthorList, Author
from resources.Books import BookList, Book
from resources.contexts import Contexts
from resources.EntryPoint import EntryPoint
import sys

app = Flask(__name__)
api = Api(app)

app.config['JSONLDIFY_MIME_TYPE'] = "application/ld+json"
app.config['CONTEXTS_FOLDER'] = "./contexts/"
app.config['API_DOC_FOLDER'] = "./api-doc/"
app.config['apiDocumentation'] = "/contexts/vocab.jsonld#"

##
## Actually setup the Api resource routing here
##
api.add_resource(EntryPoint, '/')
api.add_resource(AuthorList, '/authors/')
api.add_resource(Author, '/authors/<author_id>')
api.add_resource(BookList, '/books/')
api.add_resource(Book, '/books/<book_id>')
api.add_resource(Contexts, '/contexts/<path:contextName>')


if __name__ == '__main__':
    app.run(debug=True)