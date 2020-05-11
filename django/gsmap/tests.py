import json
import pytest
from graphene.test import Client
from main.schema import schema

@pytest.mark.django_db
def test_municipalities_exists():
    client = Client(schema)
    result = client.execute('''
query {
  municipalities {
    edges {
      node {
        id
        name
        bfsNumber
      }
    }
  }
}''',
                            context={})
    result = json.loads(json.dumps(result)) # remove OrderedDics, default in python 3.7+
    assert result == {
        "data": {
            "municipalities": {
            "edges": [
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTo2MjUy",
                    "name": "Anniviers",
                    "bfsNumber": 6252
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTo2MDMx",
                    "name": "Bagnes",
                    "bfsNumber": 6031
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTozNzky",
                    "name": "Bregaglia",
                    "bfsNumber": 3792
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTozODUx",
                    "name": "Davos",
                    "bfsNumber": 3851
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZToxNjMx",
                    "name": "Glarus Süd",
                    "bfsNumber": 1631
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTo3ODQ=",
                    "name": "Innertkirchen",
                    "bfsNumber": 784
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTozNzYy",
                    "name": "Scuol",
                    "bfsNumber": 3762
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTozNTQz",
                    "name": "Surses",
                    "bfsNumber": 3543
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTo2MzAw",
                    "name": "Zermatt",
                    "bfsNumber": 6300
                }
                },
                {
                "node": {
                    "id": "TXVuaWNpcGFsaXR5Tm9kZTozNzQ2",
                    "name": "Zernez",
                    "bfsNumber": 3746
                }
                }
            ]
            }
        }
    }


@pytest.mark.django_db
def test_snapshots_exists():
    client = Client(schema)
    result = client.execute('''
query {
    snapshots(isShowcase: true) {
        edges {
            node {
                id
                pk
                title
                topic
                screenshot
            }
        }
    }
}''',
                            context={})
    result = json.loads(
        json.dumps(result))  # remove OrderedDics, default in python 3.7+
    assert result == {
        'data': {
            'snapshots': {
                'edges': [{
                    'node': {
                        'id': 'U25hcHNob3ROb2RlOlI0UlBHQw==',
                        'pk': 'R4RPGC',
                        'title': 'test snapshot',
                        'topic': 'test topic',
                        'screenshot': ''
                    }
                }]
            }
        }
    }
