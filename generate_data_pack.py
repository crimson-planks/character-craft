import sys, json
from collections import Counter
def get_entries(name: str) -> list[dict]:
    char_count_dict=dict(Counter(name))
    result_list=[]
    for char in char_count_dict:
        tmp_dict={
            "entries": 
            [
                {
                    "type": "item",
                    "name": "recovery_compass",
                    "functions": [{"function": "set_components","components": {
                        "custom_model_data": ord(char),
                        "custom_name": '{"text":"'+char+'"}',
                        "custom_data": {"letter": True}
                    }}]
                }
            ],
            "rolls": None
        }
        tmp_dict["rolls"]=char_count_dict[char]
        result_list.append(tmp_dict)
    return result_list
block_list_file=open("block_list.json")
block_list: list[str]=json.load(block_list_file)
block_list_file.close()
def make_files():
    for block in block_list:
        loot_table_file=open(f"character_craft_data_pack/data/minecraft/loot_tables/blocks/{block}.json","w")
        tmp_dict={
            "type": "block",
            "pools": []
        }
        tmp_dict["pools"]=get_entries(block.upper())
        loot_table_file.write(json.dumps(tmp_dict))
        loot_table_file.close()
#print(get_entries("acacia_button"))
make_files()