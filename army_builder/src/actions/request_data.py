import requests
import json

url = "https://api.corvusbelli.com/army/units/es/{faction_id}"
root_assets = "./assets"
faction_file = "{assets_path}/faction_{faction_id}.json"
metadata_file = "{assets_path}/metadata.json"


def upsert_data():
    with open(metadata_file.format(assets_path=root_assets), "r") as fid:
        metadata = json.loads(fid.read())

    factions = metadata.get("factions")

    for faction in factions:
        faction_id = faction.get("id")
        response = requests.get(url.format(faction_id=faction_id))
        if response.status_code == 200:
            if "Error" in str(response.content, "utf-8"):
                continue
            request_body = response.json()
            if request_body is None:
                continue
        with open(
            faction_file.format(
                assets_path=root_assets,
                faction_id=faction_id
            ),
            "w"
        ) as fid:
            json.dump(request_body, fid)
