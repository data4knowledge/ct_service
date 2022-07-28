from py2neo.ogm import Model, Property
from neo4j.neo4j_database import Neo4jDatabase
from ra_server.ra_server import RaServer

class RegistrationAuthority(Model):

  __primarykey__ = "uuid"

  uuid = Property()
  uri = Property()
  name = Property()

  @classmethod
  def find(cls, uuid):
    db = Neo4jDatabase()
    ra = RegistrationAuthority.match(db.graph(), uuid).first()
    ra._check_complete(db)
    return ra

  def _check_complete(self, db):
    if self.name == "" or self.name == None:
      server = RaServer()
      print("RA:", self.uuid)
      ra = server.registration_authority_by_uuid(self.uuid)
      print("RA:", ra)
      self.name = ra['name']
      db.graph().push(self)