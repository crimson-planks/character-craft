import json
def put_json(ltr: str):
    jsonobj={
        "parent": "item/generated",
        "textures": {
            "layer0": f"item/{ltr}"
        }
    }
    jsonfile=None
    try:
        jsonfile=open(f"character_craft_resource_pack/assets/minecraft/models/item/{ltr}.json","w")
    except OSError:
        print("error on {ltr}.json!")
        return
    json.dump(jsonobj,jsonfile)
for char in "qwertyuiopasdfghjklzxcvbnm":
    put_json(char)