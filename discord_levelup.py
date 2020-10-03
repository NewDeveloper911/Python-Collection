from json import dumps, loads
from random import randint

def get_data():
    with open('members.json', 'r') as file:
        return loads(file.read())

def set_data(members):
    with open('members.json', 'w') as file:
        file.write(dumps(members, indent=2))

@client.event
async def on_member_join(member):
    members = self.get_data()
    members.append({'name': member.name, 'id': member.id, 'level': 0,'xp': 0})
    set_data(members)
    
@client.event
async def on_member_remove(self, member):
    members = self.get_data()
    members.remove({'name': member.name, 'id': member.id, 'level': member.level, 'xp': member.xp})
    set_data(members)

@client.event
async def on_message(message):
    members = self.get_data()
    member = members[message.author.id]
    member['xp'] += 5
    if member['xp'] > member['xp']**(1 / 4):
        member['level'] += 1
        await message.channel.send(f"🎉 {message.author.mention} leveled up! He's now level {member['level']}")
        set_data(members)

@commands.command()
async def xp(self, ctx):
    members = self.get_data()
    for member in members:
        if ctx.author.id == member['id']:
            await ctx.send(f"🎚️ You're level {member['level']} ({member['xp']}/{self.base_xp * (member['level']+1 * self.factor)})")