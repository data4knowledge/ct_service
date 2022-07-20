import pytest
from main import app
from tests.helpers.neo4j_helper import Neo4jHelper
from tests.helpers.factory import Factory
from neo4j.skos_concept import SkosConcept

def test_test():
    db = Neo4jHelper()
    db.clear()
    factory = Factory()
    skos = factory.skos_concept()
    print(skos)
    db.repository().save(skos)
    print(skos)
    x = SkosConcept.match(db.graph()).first()
    print(x)