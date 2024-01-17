# third-party imports
import json
import os


def combine_characters(directory):
  combined_data = []

  for filename in os.listdir(directory):
    if filename.endswith(".json"):
      file_path = os.path.join(directory, filename)

      with open(file_path, "r") as file:
        json_data = json.load(file)

      extracted_data = {
        "name": json_data.get("name", ""),
        "rarity": json_data.get("rarity", ""),
        "image": json_data.get("image", ""),
        "vision": json_data.get("vision", "")
      }

      combined_data.append(extracted_data)

  with open("data/character.json", "w") as combined_file:
    json.dump(combined_data, combined_file, indent=2)

  print("Characters data is successfully combined and stored in character.json")

def combine_builds(directory):
  combined_data = []

  for filename in os.listdir(directory):
    if filename.endswith(".json"):
      file_path = os.path.join(directory, filename)

      with open(file_path, "r") as file:
        json_data = json.load(file)

      combined_data.append(json_data)

  with open("data/build.json", "w") as combined_file:
    json.dump(combined_data, combined_file, indent=2)

    print("Character builds data is successfully combined and stored in build.json")

if __name__ == "__main__":
  data_directory = "data/characters"

  combine_characters(data_directory)
  combine_builds(data_directory)