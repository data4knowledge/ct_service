from py2neo.ogm import Model, Property, RelatedTo
from neo4j.semantic_version import SemanticVersion

class ScopedIdentifier(Model):
  version = Property()
  version_label = Property()
  identifier = Property()
  semantic_version = RelatedTo(SemanticVersion, "SEMANTIC_VERSION")