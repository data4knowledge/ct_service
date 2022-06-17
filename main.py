from fastapi import FastAPI
from model.system import SystemOut

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

@app.get("/terms/")
async def ct_search(code_list: str, code_list_item: str):
  # Neo4j, search db
  return {'status': "You wanted %s, %s" % (code_list, code_list_item)}