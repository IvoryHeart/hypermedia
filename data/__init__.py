books = [
	{
		"@context" : "/contexts/books.jsonld",
		"id": "1",
		"@type": "schema:Book",
		"author": "1",
		"title": "The Lord of the Rings"
	},
	{
		"@context" : "/contexts/books.jsonld",	
		"@type": "schema:Book",
		"id": "2",
		"author": "2",
		"title": "The Game of Thrones"
	}
]



authors = [
	{
		"@context" : "/contexts/authors.jsonld",
		"@type": "schema:author",
		"id": "1",
		"name": "JRR Tolkien"
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