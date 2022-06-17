from py2neo.ogm import Model, Property, RelatedTo
from neo4j.concept import Concept
from neo4j.neo4j_database import Neo4jDatabase
from model.term import Term

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
    results = db.graph().run(query).data()
    return dict(results[0]['m'])

  @classmethod
  def like(cls, term):
    results = []
    db = Neo4jDatabase()
    query = """
      MATCH (n:SkosConcept) WHERE n.pref_label CONTAINS '%s' OR n.definition CONTAINS '%s' OR n.alt_label CONTAINS '%s' RETURN n
    """ % (term, term, term)
    items = db.graph().run(query).data()
    for item in items:
      x = dict(item['n'])
      results.append(Term(**x))
    return results
