import discord
from discord import utils
import os 
import config
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Бот залогинился \n{0}'.format(self.user))
        print(client.user.id)
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = ".help"))
 
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id) # получаем объект канала
            message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
            member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
            try:
                emoji = str(payload.emoji) # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
           
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[log] Участнику - {0.display_name}, успешно была выдана роль: {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[log] У {0.display_name} слишком много ролей, что-бы выдать еще...'.format(member))
           
            except KeyError as e:
                print('[log] Не обнаруженно роли для эмодзи: ' + emoji)
            except Exception as e:
                print(repr(e))
 
    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id) # получаем объект канала
        message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
        member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
        try:
            emoji = str(payload.emoji) # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
 
            await member.remove_roles(role)
            print('[log] Роль - {1.name}, была успешно снята у участника: {0.display_name}'.format(member, role))
 
        except KeyError as e:
            print('[log] Не обнаруженно роли для эмодзи: ' + emoji)
        except Exception as e:
            print(repr(e))

# RUN
client = MyClient()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Бот залогинился \n{0}'.format(self.user))
        print(client.user.id)
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
 
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id) # получаем объект канала
            message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
            member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
            try:
                emoji = str(payload.emoji) # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
           
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[log] Участнику - {0.display_name}, успешно была выдана роль: {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[log] У {0.display_name} слишком много ролей, что-бы выдать еще...'.format(member))
           
            except KeyError as e:
                print('[log] Не обнаруженно роли для эмодзи: ' + emoji)
            except Exception as e:
                print(repr(e))
 
    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id) # получаем объект канала
        message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
        member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию
 
        try:
            emoji = str(payload.emoji) # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
 
            await member.remove_roles(role)
            print('[log] Роль - {1.name}, была успешно снята у участника: {0.display_name}'.format(member, role))
 
        except KeyError as e:
            print('[log] Не обнаруженно роли для эмодзи: ' + emoji)
        except Exception as e:
            print(repr(e))
# RUN
token = os.environ.get("BOT_TOKEN")
client = MyClient()
client.run (token)