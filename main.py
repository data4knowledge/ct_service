from fastapi import FastAPI
from model.system import SystemOut
from neo4j.neo4j_database import Neo4jDatabase
from neo4j.skos_concept import SkosConcept

VERSION = "0.1"
SYSTEM_NAME = "d4k CT Microservice"

app = FastAPI(
  title = SYSTEM_NAME,
  description = "A microservice to handle brilliant CT in a Neo4j database.",
  version = VERSION
)

@app.get("/", 
  summary="Get system and version",
  description="Returns the microservice system details and the version running.", 
  response_model=SystemOut)
async def read_root():
  #return { 'system_name': SYSTEM_NAME, 'version': VERSION }
  return SystemOut(**{ 'system_name': SYSTEM_NAME, 'version': VERSION })

@app.get("/skos_concepts/")
async def ct_search(parent: str, item: str):
  results = SkosConcept.find_within_parent(parent, item)
  return {'status': "You wanted %s" % (results)}

