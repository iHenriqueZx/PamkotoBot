import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.members = True
intents.message_content = True 
bot = commands.Bot(command_prefix="p!", intents=intents)

welcome_channel_id = Your_ID 
staff_channel_id = Your_ID   
rules_channel_id = Your_ID  
server_website = ""   

welcome_message = (
    "Seja bem-vindo {member}! \n\n"
    "Por aqui, você interage com outros jogadores da comunidade e\n"
    "fica por dentro de todas as novidades!") 

class WelcomeView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(label="Site", url=server_website, style=discord.ButtonStyle.link))
        self.add_item(Button(label="Regras", url=f"https://discord.com/channels/{bot.guilds[0].id}/{rules_channel_id}", style=discord.ButtonStyle.link))

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel_id)
    if channel:
        embed = discord.Embed(title="Bem-vindo(a)!", description=welcome_message.format(member=member.mention), color=0x18fcf2)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="IP do servidor", value="")
        view = WelcomeView()
        await channel.send(embed=embed, view=view)

@bot.event
async def on_message(message):
    if "discord.gg" in message.content.lower():
        await message.delete()
        await message.channel.send(f'{message.author.mention}, links de Discord não são permitidos.')
    await bot.process_commands(message)

def create_staff_embed(title, description, color):
    embed = discord.Embed(title=title, description=description, color=color)
    return embed

@bot.command()
@commands.has_role("GERENTE")
async def staff_saiu(ctx, member: discord.Member):
    channel = bot.get_channel(staff_channel_id)
    if channel:
        embed = create_staff_embed("📰 | STAFF LOG", f'{member.mention} saiu da equipe.', 0xAAAAAA)
        await channel.send(embed=embed)

@bot.command()
@commands.has_role("GERENTE")
async def staff_ajudante(ctx, member: discord.Member):
    channel = bot.get_channel(staff_channel_id)
    if channel:
        embed = create_staff_embed("📰 | STAFF LOG", f'{member.mention} entrou para a equipe como Ajudante.', 0xFFFF55)
        await channel.send(embed=embed)

@bot.command()
@commands.has_role("GERENTE")
async def staff_moderador(ctx, member: discord.Member):
    channel = bot.get_channel(staff_channel_id)
    if channel:
        embed = create_staff_embed("📰 | STAFF LOG", f'{member.mention} foi promovido(a) a Moderador(a).', 0x00AA00)
        await channel.send(embed=embed)

@bot.command()
@commands.has_role("GERENTE")
async def staff_admin(ctx, member: discord.Member):
    channel = bot.get_channel(staff_channel_id)
    if channel:
        embed = create_staff_embed("📰 | STAFF LOG", f'{member.mention} foi promovido(a) a Admin.', 0xFF5555)
        await channel.send(embed=embed)

@bot.command()
@commands.has_role("GERENTE")
async def staff_gerente(ctx, member: discord.Member):
    channel = bot.get_channel(staff_channel_id)
    if channel:
        embed = create_staff_embed("📰 | STAFF LOG", f'{member.mention} foi promovido(a) a Gerente.', 0xAA0000)
        await channel.send(embed=embed)

@bot.command()
@commands.has_role("GERENTE")
async def clear(ctx, amount: int):
    if amount <= 0:
        await ctx.send("Por favor, forneça um número positivo de mensagens para apagar.")
        return
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} mensagens foram apagadas.', delete_after=5)

bot.run('Your_Token')
