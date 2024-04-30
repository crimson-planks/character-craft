import sys, json
try:
    open("block_list.json").close()
except FileNotFoundError:
    print("Error: put the block_list.json into the same directory as this file")
    input("Press Enter to close.")
    sys.exit()
try:
    open("en_us.json").close()
except FileNotFoundError:
    print("Error: ")
    input("Press Enter to close.")
    sys.exit()

lang_file=open("en_us.json")
lang_text=lang_file.read()
lang_dict: dict=json.loads(lang_text)
lang_file.close()

block_list_file=open("block_list.json")
block_list_text=block_list_file.read()
block_list: list=json.loads(block_list_text)
block_list_file.close()

block_dict={}
for block in block_list:
    try:
        lang_dict["block.minecraft."+block]
    except NameError:
        pass
    block_dict[block]=lang_dict["block.minecraft."+block].upper()

block_object_file=open("block_translations.json","w")
block_object_file.write(json.dumps(block_dict))
block_object_file.close()