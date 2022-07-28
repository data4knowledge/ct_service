from typing import List
from pydantic import BaseModel
from neo4j.release import Release as nr
import json

class Release(BaseModel):
  uuid: str
  uri: str
  label: str
  consists_of: List[dict]
  identified_by: dict
  has_status: dict

class ReleaseList(BaseModel):
  label: str
  owner: str
  version: str
  date: str
  uuid: str
  items: dict

  def list():
    final_results = []
    results, map = nr.list()
    #print(json.dumps(results, indent=4, sort_keys=True))
    for result in results:
      record = {
        'label': result['identified_by']['identifier'],
        'owner': result['has_status']['managed_by']['name'], 
        'version': result['identified_by']['semantic_version'], 
        'date': result['identified_by']['version_label'],
        'uuid': result['uuid'],
        'items': {}
      }
      for item in map:
        record['items'][item] = {}
      for item in result['consists_of']:
        record['items'][item['label']]['label'] = item['identified_by']['identifier']
        record['items'][item['label']]['date'] = item['identified_by']['version_label']
        record['items'][item['label']]['uuid'] = item['uuid']
      final_results.append(record)
    return final_results
