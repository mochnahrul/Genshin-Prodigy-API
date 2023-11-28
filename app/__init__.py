# third-party imports
from flask import Flask
from flask_restx import Api
from flask_cors import CORS

# local imports
from .config import DevelopmentConfig


api = Api()

def create_app(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)

  CORS(app, resources={r"/*": {"origins": "*"}})

  api.init_app(app, version="1.0", title="Genshin Prodigy API", description="Genshin Prodigy is a valuable resource for Genshin Impact players. It offers comprehensive character build guides based on recommendations from the Genshin Impact Helper Team.")

  from .resources import build_ns, character_ns, vision_ns
  api.add_namespace(build_ns)
  api.add_namespace(character_ns)
  api.add_namespace(vision_ns)

  return app