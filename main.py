import requests

url = "https://api.corvusbelli.com/army/units/es/{faction_id}"
faction_file = "faction_{faction_id}.json"

def request_metadata():
    with open("metadata.json","r") as fid:
        metadata = json.loads(fid.read())
    
    factions =  metadata.get("factions")

    for faction in factions:
        faction_id = faction.get("id")
        requests.get(url.format(faction_id=faction_id))

        with open(faction_file.format(faction_id=faction_id), "w") as fid:
            json.dump(fid, requests.json())