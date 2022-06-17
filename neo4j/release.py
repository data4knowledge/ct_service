from py2neo.ogm import Model, Property, RelatedTo
from neo4j.concept import Concept
from neo4j.skos_concept_scheme import SkosConceptScheme

class Release(Concept):
  consists_of = RelatedTo(SkosConceptScheme, "CONSISTS_OF")