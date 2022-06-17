from fastapi import FastAPI

VERSION = "0.1"
SYSTEM_NAME = "d4k CT Microservice"

app = FastAPI(
  title = SYSTEM_NAME,
  description = "A microservice to handle brilliant CT in a Neo4j database.",
  version = VERSION
)

@app.get("/")
async def read_root():
  return { 'system_name': SYSTEM_NAME, 'version': VERSION }
