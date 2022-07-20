import pytest
from main import app
from tests.helpers.neo4j_helper import Neo4jHelper

def test_test():
    db = Neo4jHelper()
    db.clear()
