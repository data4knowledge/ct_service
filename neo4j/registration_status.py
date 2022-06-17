from py2neo.ogm import Model, Property

class RegistrationStatus(Model):
  registration_status = Property()
  effective_date = Property()
  until_date = Property()
