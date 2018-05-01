from .data import books, authors
from flask_restful import Resource, abort, reqparse
import sys
from ldify import ld_response, JSONLDIFY_MIME_TYPE

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('id')
parser.add_argument('description')

contextPath="/contexts/books.jsonld"
apiDocumentation = "/contexts/vocab.jsonld#"

# BooksList
# shows a list of all books, and lets you POST to add new tasks
class BookList(Resource):
    def get(self):
        return ld_response(books, 200, context=contextPath, apiDoc=apiDocumentation)

    def post(self):
        args = parser.parse_args()
        book_id = len(books) + 1
        #book_id = 'books/%i' % todo_id
        book = {'id': book_id, 'title': args['title']}
        books.append(book)
        #return book, 201
        return ld_response(book, 201, context=contextPath, apiDoc=apiDocumentation)

class Book(Resource):
    def get(self, book_id):
        book, index = abort_if_book_doesnt_exist(book_id)
        #return book, 200
        return ld_response(book, 200, context=contextPath, apiDoc=apiDocumentation)

    def delete(self, book_id):
    	book, index = abort_if_book_doesnt_exist(book_id)
    	#del books[book_id]
    	books.pop(index)
    	#return '', 204
    	return ld_response('', 204, context=contextPath, apiDoc=apiDocumentation)

    def post(self, book_id):
        args = parser.parse_args()
        #book, index = book_find(book_id)
        book, index = abort_if_book_doesnt_exist(book_id)
        #book = {'id': book_id, 'name': args['name']}
        print ("ARGS:: ", file=sys.stderr)
        print (args, file=sys.stderr)
        print ("book:: ", file=sys.stderr)
        print ( book, file=sys.stderr)

        for key, value in args.items():
            if key in args and value is not None:
                book[key] = value

        books[index] = book
        #return books[book_id], 200
        return ld_response(book, 200, context=contextPath, apiDoc=apiDocumentation)

    def put(self, book_id):
        args = parser.parse_args()
    	#PUT is idempotent and it should take id in the request itself.
    	#book, index = book_find(book_id)
        book, index = abort_if_book_doesnt_exist(book_id)
        
        book = {'id': int(args['id']), 'name': args['name']}

        books.append(book)
    	#return book, 201
        return ld_response(book, 200, context=contextPath, apiDoc=apiDocumentation)

def abort_if_book_doesnt_exist(book_id):
    book, index = book_find(book_id)
    if book is None:
        abort(404, message="book {} doesn't exist".format(book_id))
        #ld_response("book {} doesn't exist".format(book_id), status=404)
    else: 
        return book, index

def book_find(book_id):
    for index, book in enumerate(books):
        print(book, file=sys.stderr)
        if book['id'] == int(book_id) or book['id'] == book_id:
            return book, index
    return None, -1