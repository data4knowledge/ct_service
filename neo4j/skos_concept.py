from py2neo.ogm import Model, Property, RelatedTo
from neo4j.concept import Concept
from neo4j.neo4j_database import Neo4jDatabase

class SkosConcept(Concept):
  identifier = Property()
  notation = Property()
  alt_label = Property()
  pref_label = Property()
  definition = Property()

  narrower = RelatedTo('SkosConcept', "NARROWER")

  @classmethod
  def find_within_parent(cls, parent_identifier, identifier):
    db = Neo4jDatabase()
    query = """
      MATCH (n:SkosConcept)-[:NARROWER]->(m:SkosConcept) WHERE n.identifier='%s' AND m.identifier='%s' RETURN m
    """ % (parent_identifier, identifier)
    results = db.graph().run(query)
    return results