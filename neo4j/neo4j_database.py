from py2neo.ogm import Repository
import os

DB_NAME = "neo4j"

class Neo4jDatabase():
  
  def __init__(self):
    url = os.environ['CT_SERVICE_NEO4J_URL']
    usr = os.environ['CT_SERVICE_NEO4J_USER']
    pwd = os.environ['CT_SERVICE_NEO4J_PWD']
    self.__repo = Repository(url, name=DB_NAME, user=usr, password=pwd)

  def repository(self):
    return self.__repo

  def graph(self):
    return self.__repo.graph

  def clear(self):
    query = """
      CALL apoc.periodic.iterate('MATCH (n) RETURN n', 'DETACH DELETE n', {batchSize:1000})
    """
    self.__repo.graph.run(query)
