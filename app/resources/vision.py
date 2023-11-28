# third-party imports
import json
from flask_restx import Resource, Namespace

# local imports
from .. import api
from ..utils import normalize_name


vision_ns = Namespace("Vision", path="/vision", description="Operations about Vision")

# load data from JSON file
data = []
with open("app/data/vision.json", "r") as file:
  data = json.load(file)

@vision_ns.route("")
class VisionList(Resource):
  def get(self):
    """Get a list of all visions."""
    sorted_data = sorted(data, key=lambda x: x["name"].lower())
    return sorted_data

@vision_ns.route("/<name>")
@vision_ns.doc(responses={404: "Vision not found"}, params={"name": "Vision Name"})
class VisionResource(Resource):
  def get(self, name):
    """Get vision by Name."""
    normalized_name = normalize_name(name)
    vision = next((vis for vis in data if normalize_name(vis["name"]) == normalized_name), None)
    if not vision:
      api.abort(404, "Vision with name {} not found".format(name))
    return vision