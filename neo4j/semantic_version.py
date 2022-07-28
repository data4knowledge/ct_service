from py2neo.ogm import Model, Property

class SemanticVersion(Model):
  major = Property()
  minor = Property()
  patch = Property()

  def __init__(self, version):
    self.major = '0'
    self.minor = '0'
    self.patch = '0'
    parts = version.split(".")
    if len(parts) == 0:
      pass
    elif len(parts) == 1:
      self.major = parts[0]
    elif len(parts) == 2:
      self.major = parts[0]
      self.minor = parts[1]
    elif len(parts) == 2:
      self.major = parts[0]
      self.minor = parts[1]
      self.patch = parts[2]

  def __str__(self):
    return "%s.%s.%s" % (self.major, self.minor, self.patch)