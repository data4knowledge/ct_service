from py2neo.ogm import Model, Property

class SemanticVersion(Model):
  major = Property()
  minor = Property()
  patch = Property()
