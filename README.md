# py-sysml-rdf

A Python library providing RDF ontology definitions for SysML (Systems Modeling Language). This library contains a generated TTL (Turtle) file with SysML ontology definitions and provides a convenient Python interface to access the ontology classes and properties.

## Ontology Visualization

Visualized the ontology with [WebVOWL](https://service.tib.eu/webvowl/)

![SysML Ontology](./sysml-0.0.2.ttl.svg)


## Installation

```bash
pip install py-sysml-rdf
```

## Usage

```python
from py_sysml_rdf import SYSML
from rdflib import URIRef, Graph, RDF

g = Graph()
g.bind("sysml", SYSML._NS)
g.add((URIRef("http://example.org#actor_x"), RDF.type, SYSML.Actor))

```

## Development


### Regenerating the Ontology

If you need to recreate the TTL file:

```bash
python create_sysml_ontology.py
```


### Testing

Run the test script to verify everything works:

```bash
python -m pytest tests/
```
### Building the Package

```bash
poetry build
```

### Publish the Package
```bash
poetry publish --username __token__ --password <TOKEN>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)