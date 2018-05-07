# hypermedia
Experiments on hypermeda.

Starting with python flask for rapid prototyping.

Added JSON-LD and Hydra support.

Need to add DB support.

## JSON-LD

### Learnings/Cheat sheet

#### Lists
* Values can be single or multiple (lists)
* For explicit lists, use @container
```
{
    "@context": {
        "members": {
            "@id": "hydra:member",
            "@type": "@id",
            "@container" : "@list"
        }
        ...
    }
    ...
}
```