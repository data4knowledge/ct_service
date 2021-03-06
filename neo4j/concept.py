from py2neo.ogm import Model, Property, RelatedTo
from neo4j.scoped_identifier import ScopedIdentifier
from neo4j.registration_status import RegistrationStatus
from neo4j.extension import Extension

class Concept(Model):
  uuid = Property()
  uri = Property()
  label = Property()
  
  identified_by = RelatedTo(ScopedIdentifier, "IDENTIFIED_BY")
  has_status = RelatedTo(RegistrationStatus, "HAS_STATUS")
  previous = RelatedTo('Concept', "PREVIOUS")
  extended_with = RelatedTo(Extension, "EXTENDED_WITH")