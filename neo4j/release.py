from py2neo.ogm import Model, Property, RelatedTo
from neo4j.neo4j_database import Neo4jDatabase
from neo4j.concept import Concept
from neo4j.registration_authority import RegistrationAuthority
from neo4j.scoped_identifier import ScopedIdentifier
from neo4j.skos_concept_scheme import SkosConceptScheme

class Release(Concept):
  consists_of = RelatedTo(SkosConceptScheme, "CONSISTS_OF")

  @classmethod
  def list(cls):
    release_map = {}
    consists_map = {}
    results = []
    db = Neo4jDatabase()
    query = """
      MATCH (ni:ScopedIdentifier)<-[:IDENTIFIED_BY]-(n:Release)-[:CONSISTS_OF]->(m:SkosConceptScheme)-[:IDENTIFIED_BY]->(mi:ScopedIdentifier), 
        (n)-[:HAS_STATUS]->(ns:RegistrationStatus)-[:MANAGED_BY]->(ra:RegistrationAuthority) 
        RETURN n,ni,m,mi,ns,ra ORDER BY ni.version, mi.version
    """
    query_results = db.graph().run(query).data()
    for query_result in query_results:
      rel_uuid = query_result['n']['uuid']
      if not rel_uuid in release_map:
        rel = dict(query_result['n'])
        rel['identified_by'] = dict(query_result['ni'])
        rel['has_status'] = dict(query_result['ns'])
        ra = RegistrationAuthority.find(query_result['ra']['uuid'])
        rel['has_status']['managed_by'] = dict(ra.__node__)
        rel['consists_of'] = []
        release_map[rel_uuid] = rel
        results.append(rel)
      else:
        rel = release_map[rel_uuid]
      cs = dict(query_result['m'])  
      consists_map[cs['label']] = cs['label']
      cs['identified_by'] = dict(query_result['mi'])
      rel['consists_of'].append(cs)
    return results, consists_map.keys()