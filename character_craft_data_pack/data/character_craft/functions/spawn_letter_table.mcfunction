kill @e[type=item,nbt={Item:{id:"minecraft:recovery_compass",components:{custom_model_data:76,custom_data:{letter:1b}},count:2b}},sort=nearest,limit=1]
kill @e[type=item,nbt={Item:{id:"minecraft:recovery_compass",components:{custom_model_data:69,custom_data:{letter:1b}},count:3b}},sort=nearest,limit=1]
kill @e[type=item,nbt={Item:{id:"minecraft:recovery_compass",components:{custom_model_data:84,custom_data:{letter:1b}},count:3b}},sort=nearest,limit=1]
kill @e[type=item,nbt={Item:{id:"minecraft:recovery_compass",components:{custom_model_data:82,custom_data:{letter:1b}},count:1b}},sort=nearest,limit=1]
kill @e[type=item,nbt={Item:{id:"minecraft:recovery_compass",components:{custom_model_data:65,custom_data:{letter:1b}},count:1b}},sort=nearest,limit=1]
kill @e[type=item,nbt={Item:{id:"minecraft:recovery_compass",components:{custom_model_data:66,custom_data:{letter:1b}},count:1b}},sort=nearest,limit=1]

summon item ~ ~ ~ {Item:{id:"bat_spawn_egg",count:1b,components:{custom_model_data:7684,custom_name:'{"text": "Letter Table","italic": false}',entity_data:{id:"marker",Tags:["LetterTableMarker"]}}}}
playsound block.nether_wood.place block @a ~ ~ ~ 16 2
playsound block.basalt.place block @a ~ ~ ~ 16 2
kill @s