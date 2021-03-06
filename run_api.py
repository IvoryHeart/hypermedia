from hypermedia import app, api 

app.config['JSONLDIFY_MIME_TYPE'] = "application/ld+json"
app.config['CONTEXTS_FOLDER'] = "./contexts/"
app.config['API_DOC_FOLDER'] = "./api-doc/"
app.config['hydra:apiDocumentation'] = "/contexts/vocab.jsonld#"
app.config['dbType'] = "object"


## Import other objects dependent on app context

from hypermedia.resources.Authors import AuthorCollection, Author
from hypermedia.resources.Books import BookCollection, Book
from hypermedia.resources.contexts import Contexts
from hypermedia.resources.EntryPoint import EntryPoint

##
## Actually setup the Api resource routing here
##
api.add_resource(EntryPoint, '/')
api.add_resource(AuthorCollection, '/authors/')
api.add_resource(Author, '/authors/<author_id>')
api.add_resource(BookCollection, '/books/')
api.add_resource(Book, '/books/<book_id>')
api.add_resource(Contexts, '/contexts/<path:contextName>')


if __name__ == '__main__':
    app.run(debug=True)