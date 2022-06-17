from fastapi import FastAPI
from model.system import SystemOut
from model.term import Term
from neo4j.neo4j_database import Neo4jDatabase
from neo4j.skos_concept import SkosConcept
from fastapi_pagination import Page, add_pagination, paginate

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
async def ct_term(parent: str, item: str):
  return SkosConcept.find_within_parent(parent, item)

@app.get("/skos_concepts/like", response_model=Page[Term])
async def ct_like(text: str):
  return paginate(SkosConcept.like(text))

add_pagination(app)