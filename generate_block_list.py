import os, sys, re, json
try:
    open("dirt.json").close()
except FileNotFoundError:
    print("Error: put generate_block_list.py in (your minecraft directory)/versions/(Your minecraft version)/(unzip the .jar file and open it)/data/minecraft/loot_tables/blocks and then run it")
    input("Press Enter to close.")
    sys.exit()
block_list=[]
file_list=os.listdir()
for file_name in file_list:
    if(re.search(".json$",file_name)):
        block_list.append(file_name[:-5])
block_list.sort()
result_file=open("block_list.json","w")
result_file.write(json.dumps(block_list))
result_file.close()