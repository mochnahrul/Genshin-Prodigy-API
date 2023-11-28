# third-party imports
import json
from flask_restx import Resource, Namespace

# local imports
from .. import api
from ..utils import normalize_name


build_ns = Namespace("Build", path="/build", description="Operations about Character Build")

# load data from JSON file
data = []
with open("app/data/build.json", "r") as file:
  data = json.load(file)

@build_ns.route("")
class BuildList(Resource):
  def get(self):
    """Get a list of all character builds."""
    sorted_data = sorted(data, key=lambda x: (-x["rarity"], x["name"].lower()))
    return sorted_data

@build_ns.route("/<name>")
@build_ns.doc(responses={404: "Character not found"}, params={"name": "Character Name"})
class BuildResource(Resource):
  def get(self, name):
    """Get character build by Character Name."""
    normalized_name = normalize_name(name)
    character = next((char for char in data if normalize_name(char["name"]) == normalized_name), None)
    if not character:
      api.abort(404, "Character with name {} not found".format(name))
    return character