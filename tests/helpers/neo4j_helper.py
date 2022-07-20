from py2neo.ogm import Repository
import os

DB_NAME = "neo4j"

class Neo4jHelper():
  
  def __init__(self):
    url = "neo4j://localhost:7687"
    usr = "neo4j"
    pwd = "neo4j"
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
