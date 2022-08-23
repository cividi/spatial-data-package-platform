import os
import json
import base64
from celery import shared_task
import requests
from main.settings import API_CACHE_ROOT


@shared_task
def update_cache(ws_hash, lang):
    query = """query getworkspace($wshash: ID!, $lang: LanguageCodeEnum!) {
      workspace(id: $wshash) {
        id
        pk
        title
        description
        mode
        findmeEnabled
        annotationsOpen
        annotationsLikesEnabled
        polygonOpen
        polygonLikesEnabled
        objectOpen
        objectLikesEnabled
        objectsPageLink
        snapshots {
          id
          pk
          title
          topic
          screenshot
          thumbnail
          datafile
          municipality {
            bfsNumber
            fullname
          }
        }
        categories {
          pk
          color
          name(languageCode: $lang)
          hideInList
          hideInLegend
          icon
        }
        states {
          pk
          name(languageCode: $lang)
          decoration
          hideInList
          hideInLegend
        }
        spatialDatasettes {
          name
          baseUrl
          queries
        }
        usergroups {
          key
          name(languageCode: $lang)
        }
        annotations {
          id
          pk
          kind
          rating
          data
          category {
            pk
            name(languageCode: $lang)
            icon
            color
            commentsEnabled
          }
          state {
            pk
            name(languageCode: $lang)
            decoration
          }
          attachements {
            document
            myOrder
          }
        }
      }
    }"""

    wshash_base64 = base64.urlsafe_b64encode(f"WorkspaceNode:{ws_hash}".encode("utf-8"))

    r = requests.post(
        f"http://django:8081/graphql/",
        json = {
            'query': query,
            'variables': {
                'wshash': str(wshash_base64, "utf-8"),
                'lang': lang
            }
        }
    )
    
    os.makedirs(f"{API_CACHE_ROOT}/{lang}", exist_ok = True)

    with open(f"{API_CACHE_ROOT}/{lang}/{ws_hash}.json", "w") as file:
      json.dump(r.json(), file)
    
    return r.json()
