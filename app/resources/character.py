# third-party imports
import json
from flask_restx import Resource, Namespace

# local imports
from .. import api
from ..utils import normalize_name


character_ns = Namespace("Character", path="/character", description="Operations about Character")

# load data from JSON file
data = []
with open("app/data/character.json", "r") as file:
  data = json.load(file)

@character_ns.route("")
class CharacterList(Resource):
  def get(self):
    """Get a list of all characters."""
    sorted_data = sorted(data, key=lambda x: (-x["rarity"], x["name"].lower()))
    return sorted_data

@character_ns.route("/<name>")
@character_ns.doc(responses={404: "Character not found"}, params={"name": "Character Name"})
class CharacterResource(Resource):
  def get(self, name):
    """Get character by Character Name."""
    normalized_name = normalize_name(name)
    character = next((char for char in data if normalize_name(char["name"]) == normalized_name), None)
    if not character:
      api.abort(404, "Character with name {} not found".format(name))
    return character