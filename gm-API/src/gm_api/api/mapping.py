import falcon
import json
from random import randint, choice


quotes = [
    '"Kicking ass takes getting your ass kicked" ~ Jason Calacanis',
    '"The perfect is the enemy of the good." ~ Voltaire',
    '"In essence, if we want to direct our lives, we must take control of our\
    consistent actions. It\'s not what we do once in a while that shapes our\
    lives, but what we do consistently." ~ Tony Robbins'
    ]

mock_response = {'id': randint(0, 200), 'status': choice(quotes)}


class Mapping(object):
    """Create Mapping class."""

    def on_post(self, req, resp):
        """Respond on GET request to map endpoint."""
        resp.data = json.dumps(mock_response)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_202


class MappingResource(object):
    """Create Mapping Resource based on ID for retrieval."""

    def on_get(self, req, resp, mapID):
        """Respond on GET request to map endpoint."""
        resp.data = json.dumps(mock_response)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, mapID):
        """Respond on GET request to map endpoint."""
        resp.data = json.dumps(mock_response)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
