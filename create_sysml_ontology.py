from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, DCTERMS, Literal, XSD
import tomllib

with open("pyproject.toml", "rb") as f:
    pyproject_data = tomllib.load(f)


KEY = "sysml"

# Definition des NameNSraums
NS = Namespace(f"http://frittenburger.de/ontology/{KEY}#")

# Erstellung des Graphen
g = Graph()
g.namespace_manager.bind(KEY, NS)

# Ontology
ontology = URIRef(f"https://gitlab.hpi.de/dfriedenberger/{KEY}")
g.add((ontology, RDF.type, OWL.Ontology))
g.add((ontology, DCTERMS.title, Literal("SysML Ontology")))
g.add((ontology, DCTERMS.description, Literal("A rdf Ontology for SysML model.", lang='en')))

g.add((ontology, OWL.versionInfo, Literal(pyproject_data['tool']['poetry']['version'])))
g.add((ontology, DCTERMS.creator, Literal("Dirk Friedenberger")))
g.add((ontology, DCTERMS.creator, URIRef("https://www.researchgate.net/profile/Dirk_Friedenberger")))
g.add((ontology, DCTERMS.identifier, Literal(NS)))

# concepts

# UseCases
g.add((NS.Actor, RDF.type, OWL.Class))
g.add((NS.Actor, RDFS.label, Literal("An use case actor.", lang='en')))

g.add((NS.UseCase, RDF.type, OWL.Class))
g.add((NS.UseCase, RDFS.label, Literal("An use case.", lang='en')))

g.add((NS.Subject, RDF.type, OWL.Class))
g.add((NS.Subject, RDFS.label, Literal("An use case subject.", lang='en')))


# Block Definition
g.add((NS.Block, RDF.type, OWL.Class))
g.add((NS.Block, RDFS.label, Literal("A system component.", lang='en')))

# Requirements
g.add((NS.Requirement, RDF.type, OWL.Class))
g.add((NS.Requirement, RDFS.label, Literal("A requirement.", lang='en')))

g.add((NS.requirementId, RDF.type, OWL.DatatypeProperty))
g.add((NS.requirementId, RDFS.domain, NS.Requirement))
g.add((NS.requirementId, RDFS.range, XSD.string))

g.add((NS.requirementText, RDF.type, OWL.DatatypeProperty))
g.add((NS.requirementText, RDFS.domain, NS.Requirement))
g.add((NS.requirementText, RDFS.range, XSD.string))


# relations
g.add((NS.association, RDF.type, OWL.ObjectProperty))
g.add((NS.association, RDFS.domain, NS.Block))
g.add((NS.association, RDFS.range, NS.Block))
g.add((NS.association, RDFS.label, Literal("Association between blocks", lang='en')))

g.add((NS.composition, RDF.type, OWL.ObjectProperty))
g.add((NS.composition, RDFS.domain, NS.Block))
g.add((NS.composition, RDFS.range, NS.Block))
g.add((NS.composition, RDFS.label, Literal("Composition between blocks", lang='en')))
g.add((NS.composition, RDFS.subPropertyOf, NS.association))


g.add((NS.shared, RDF.type, OWL.ObjectProperty))
g.add((NS.shared, RDFS.domain, NS.Block))
g.add((NS.shared, RDFS.range, NS.Block))
g.add((NS.shared, RDFS.label, Literal("Shared between blocks", lang='en')))
g.add((NS.shared, RDFS.subPropertyOf, NS.association))

g.add((NS.hasSubject, RDF.type, OWL.ObjectProperty))
g.add((NS.hasSubject, RDFS.domain, NS.UseCase))
g.add((NS.hasSubject, RDFS.range, NS.Subject))
g.add((NS.hasSubject, RDFS.label, Literal("hasSubject", lang='en')))

g.add((NS.nestedRequirement, RDF.type, OWL.ObjectProperty))
g.add((NS.nestedRequirement, RDFS.domain, NS.Requirement))
g.add((NS.nestedRequirement, RDFS.range, NS.Requirement))
g.add((NS.nestedRequirement, RDFS.label, Literal("nestedRequirement", lang='en')))





# Serialisierung der Ontologie in RDF/XML-Syntax
g.serialize(destination=f"py_sysml_rdf/{KEY}.ttl", format='turtle')
