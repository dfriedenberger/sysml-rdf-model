from pathlib import Path
from rdflib.namespace import DefinedNamespace
from rdflib import URIRef
from .ontology_reader import OntologyReader

# Absoluten Pfad zum aktuellen Skript-Verzeichnis bestimmen
current_dir = Path(__file__).parent

# TTL-Datei im gleichen Verzeichnis finden
ontology_file = current_dir / "sysml.ttl"
ontology = OntologyReader(str(ontology_file))


class SYSML(DefinedNamespace):

    _NS = ontology.get_namespace()

    Actor: URIRef = ontology.get_class('#Actor')
    UseCase: URIRef = ontology.get_class('#UseCase')
    Subject: URIRef = ontology.get_class('#Subject')
    Requirement: URIRef = ontology.get_class('#Requirement')
    Block: URIRef = ontology.get_class('#Block')

    association: URIRef = ontology.get_object_property('#association')
    composition: URIRef = ontology.get_object_property('#composition')
    shared: URIRef = ontology.get_object_property('#shared')
    
    hasSubject: URIRef = ontology.get_object_property('#hasSubject')
    nestedRequirement: URIRef = ontology.get_object_property('#nestedRequirement')

    requirementId: URIRef = ontology.get_datatype_property('#requirementId')
    requirementText: URIRef = ontology.get_datatype_property('#requirementText')
