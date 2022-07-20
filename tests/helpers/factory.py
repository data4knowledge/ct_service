from neo4j.skos_concept import SkosConcept

class Factory():
  
  def skos_concept(self, **kwargs):
    object = SkosConcept()
    self.set_attribute(object, 'identifier', kwargs, "A12345")
    self.set_attribute(object, 'notation', kwargs, "NOTATION")
    self.set_attribute(object, 'pref_label', kwargs, "PT")
    self.set_attribute(object, 'alt_label', kwargs, ["ALT"])
    self.set_attribute(object, 'definition', kwargs, 'Definition')
    return object

  def set_attribute(self, object, name, kwargs, default):
    if name in kwargs:
      setattr(object, name, kwargs[name])
    else:
      setattr(object, name, default)
