books = [
	{
		"@context" : "/contexts/books.jsonld",
		"@type": "schema:Book",
		
		"id": "1",
		"author": "/authors/1",
		"title": "The Lord of the Rings"
	},
	{
		"@context" : "/contexts/books.jsonld",	
		"@type": "schema:Book",
		"id": "2",
		"author": ["/authors/2","/authors/1"],
		"title": "The Game of Thrones"
	}
]


"""
Removing @type will not make documentation jump
"""

authors = [
	{
		"@context" : "/contexts/authors.jsonld",
		"@type": "schema:author",
		"id": "1",
		"name": "JRR Tolkien Sr."
	},
	{
		"@context" : "/contexts/authors.jsonld",	
		"@type": "schema:author",
		"id": "2",
		"name": "George RR Martin"
	}
]

# entryPoint = {
#   "@context": "/contexts/EntryPoint.jsonld",
#   "@id": "/",
#   "@type": "vocab:EntryPoint",
#   "authors": "/authors/"
# }

entryPoint = {
  "@context": {
		"hydra": "http://www.w3.org/ns/hydra/core#",
		"ask": "http://localhost:5000/",
		"vocab": "ask:contexts/vocab.jsonld#",
		"authors": {
			"@id": "vocab:EntryPoint/authors",
			"@type": "@id"
		},
		"books": {
			"@id": "vocab:EntryPoint/books",
			"@type": "@id"
		}
  },
  "@id": "/",
  "@type": "vocab:EntryPoint",
  "authors": "/authors/",
  "books": "/books/"
}