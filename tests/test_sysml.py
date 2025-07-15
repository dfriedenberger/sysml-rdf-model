from py_sysml_rdf import SYSML
from rdflib import URIRef, Graph, RDF


def test_namespace_exists():
    """Test that the SYSML namespace is properly defined."""
    assert SYSML._NS is not None
    assert str(SYSML._NS).startswith("http://")


def test_classes_exist():
    """Test that all expected classes are defined."""
    assert isinstance(SYSML.Actor, URIRef)
    assert isinstance(SYSML.UseCase, URIRef)
    assert isinstance(SYSML.Subject, URIRef)
    assert isinstance(SYSML.Requirement, URIRef)


def test_object_properties_exist():
    """Test that all expected object properties are defined."""
    assert isinstance(SYSML.association, URIRef)
    assert isinstance(SYSML.hasSubject, URIRef)
    assert isinstance(SYSML.nestedRequirement, URIRef)


def test_datatype_properties_exist():
    """Test that all expected datatype properties are defined."""
    assert isinstance(SYSML.requirementId, URIRef)
    assert isinstance(SYSML.requirementText, URIRef)


def test_workflow():
    g = Graph()
    g.bind("sysml", SYSML._NS)
    g.add((URIRef("http://example.org#actor_x"), RDF.type, SYSML.Actor))

    assert (URIRef("http://example.org#actor_x"), RDF.type, SYSML.Actor) in g
