import discord
from discord.ext import commands

descrition = "le bot de la galaxie"
bot_prefix = "."

server_id = 450763546188447745

message_aide = "ceci est un message d'aide :\ncommande:\n.aled : affiche ce mesage\n.add_role : permet d'atribuer les grade d'acces au channel\n.aled_role : aide pour la commande de role"
message_aide_role1 = "1:Soldat Rebelle\n2:Soldat Imperial\n3:porn role place holder\n4:hentai role place holder\n5:hentai chelou place holder\n" 
message_aide_role2 = "6:weeb\n7:Yugi Ho\n8:csgo\n9:LoL\n10:Overwatch\n11:WoW\n12:FE\n13:channel prog\n"
message_aide_role3 = "utilisation de la commande :\n.add_role 1 3 7 13 8\ncela vous attribura les grade n°1 3 7 13 8 de la liste si dessus\n"
message_aide_role4 = "pour certain grade un appel a un admin sera obligatoire"
message_aide_role = message_aide_role1 + message_aide_role2 + message_aide_role3 + message_aide_role4
my_bot = commands.Bot(descrition=descrition,command_prefix=bot_prefix)

@my_bot.event
async def on_ready():
	print("logged in")
	print("name : {}".format(my_bot.user.name))
	print("ID : {}".format(my_bot.user.id))
	print(discord.__version__)

@my_bot.command(pass_context=True)
async def aled(ctx):
	await my_bot.send_message(ctx.message.author,message_aide)
	
@my_bot.command(pass_context=True)
async def aled_role(ctx):
	await my_bot.send_message(ctx.message.author,message_aide_role)

@my_bot.command(pass_context=True)
async def oui(ctx):
	await my_bot.say("{}".format("Oui!"))

@my_bot.command(pass_context=True)
async def add_role(ctx):
	list_role = list()
	list_role.clear()
	list_role.append(discord.utils.get(ctx.message.server.roles,name="Soldat Rebelle"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="Soldat Imperial"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="porn role place holder"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="hentai role place holder"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="hentai chelou place holder"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="weeb"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="Yugi Ho"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="csgo"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="LoL"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="Overwatch"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="WoW"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="fin stratege"))
	list_role.append(discord.utils.get(ctx.message.server.roles,name="prog"))

	error_flag = False
	error_message = ""
	temp = ctx.message.content
	temp = temp.replace(".add_role ","");
	temp += "*"
	print(temp)
	role_to_assign_array_int = list()
	role_to_assign_array_role = list()
	i=0

	while(temp[i] != "*" and not error_flag):

		if(temp[i] != " "):
			role_to_assign_array_int.append(int(temp[i]) - 1)
		i = i + 1

	for role in role_to_assign_array_int:
		role_to_assign_array_role.append(list_role[role])

	if(error_flag):
		await my_bot.send_message(ctx.message.author,error_message)
	else:
		
		#for role in role_to_assign_array_role:
			
			#await my_bot.add_roles(ctx.message.author,role)
		await my_bot.add_roles(ctx.message.author,*role_to_assign_array_role)





my_bot.run("NDQ3NzIxNzczODE2MDg2NTI4.DeLwCg.2SlzyL1ogMsh-GVxlkKz8I3EK0U")