books = [
	{
		"@type": "http://schema.org/Book",
		"@id": "./1",
		"id": 1,
		"author_id": 1,
		"title": "The Lord of the Rings"
	},
	{
		"@type": "http://schema.org/Book",
		"@id": "./2",	
		"id": 2,
		"author_id": 2,
		"title": "The Game of Thrones"
	}
]



authors = [
	{
		"@type": "http://schema.org/author",
		"@id": "./1",
		"id": 1,
		"name": "JRR Tolkien"
	},
	{
		"@type": "http://schema.org/author",
		"@id": "./2",
		"id": 2,
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