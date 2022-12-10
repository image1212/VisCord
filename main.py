import discord
from discord.ext import commands
import requests
import random

#############################
#            설정            #
token = "토큰"
prefix = "V."
accountnumber = "계좌번호"
#            설정            #
#############################

bot = commands.Bot(self_bot=True, command_prefix=prefix, help_command=None)
hide = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _"
blue = "5865F2"
red = "ED4245"
green = "57F287"
def embed(desc,color):
    start = str(desc)
    end = start.replace(" " , "%2520").replace(">" , "%253E").replace("<" , "%253C").replace("\n" , "%255").replace("/" , "%253A").replace("?" , "%252F").replace("=" , "%253F").replace("_" , "%253D_")
    if color == "blue":
        return(f"https://rauf.wtf/embed/?title=VisCord&description={end}&color={blue}&redirect=https%253A%252F%252Fgithub.com%252Fimage1212")
    elif color == "red":
        return(f"https://rauf.wtf/embed/?title=Error&description={end}&color={red}&redirect=https%253A%252F%252Fgithub.com%252Fimage1212")
    elif color == "green":
        return(f"https://rauf.wtf/embed/?title=Success&description={end}&color={green}&redirect=https%253A%252F%252Fgithub.com%252Fimage1212")

@bot.event
async def on_ready():
    print(f"> VCord V1 - ㅠㅠ미지#3270 <")
    print(f"> 로딩된 이름 : {bot.user} ID : {bot.user.id} <")
    print(f"> 셀프봇이 켜졌습니다 <")

@bot.event
async def on_command_error(ctx, error):
    if ctx.author.id == bot.user.id:
        em = embed(f"> {error}","red")
        await ctx.send(f"> 에러"+hide+em)

@bot.command()
async def VisCord(ctx):
    if ctx.author.id == bot.user.id:
        em = embed("> 👋 반가워요 <","blue")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}VisCord"+hide+em)

@bot.command()
async def 상태변경(ctx, name, status):
    if ctx.author.id == bot.user.id:
        if status == "하는중":
            await bot.change_presence(activity=discord.Game(name=name))
            em = embed(f"> 상태를 '{name} 하는중' 으로 바꿨습니다 ! <","green")
        elif status == "방송중":
            await bot.change_presence(activity=discord.Streaming(name=name, url="https://www.twitch.tv/kanetv8"))
            em = embed(f"> 상태를 '{name} 방송중' 으로 바꿨습니다 ! <","green")
        elif status == "듣는중":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
            em = embed(f"> 상태를 '{name} 듣는중' 으로 바꿨습니다 ! <","green")
        elif status == "시청중":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
            em = embed(f"> 상태를 '{name} 시청중' 으로 바꿨습니다 ! <","green")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}상태변경 {name} {status}"+hide+em)

@bot.command()
async def 로블랜계(ctx):
    if ctx.author.id == bot.user.id:
        re = requests.get(f'https://api.bloxalts.xyz/v1/generate/1')
        if re.status_code == 200:
            account = re.json()["accounts"][0]
            data = requests.get(f'https://api.bloxalts.xyz/v1/format/{account}')
            username = data.json()["username"]
            password = data.json()["password"]
            em = embed(f"{username}:{password}","green")
        else:
            em = embed(f"> 계정 생성 실패 !' <","red")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}로블랜계"+hide+em)

@bot.command()
async def 토큰체킹(ctx, chtoken):
    if ctx.author.id == bot.user.id:
        headers = {'Content-Type': 'application/json', 'authorization': chtoken}
        url = 'https://discordapp.com/api/v6/users/@me/library'
        re = requests.get(url, headers=headers)
        if re.status_code == 200:
            em = embed(f"> 토큰이 살아있음 ! <","green")
        else:
            em = embed(f"> 토큰이 죽어있음 ! <","green")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}토큰체킹 (토큰)"+hide+em)

@bot.command()
async def 내계좌(ctx):
    if ctx.author.id == bot.user.id:
        em = embed(f"> {accountnumber} <","blue")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}내계좌"+hide+em)

@bot.command()
async def 핑(ctx):
    if ctx.author.id == bot.user.id:
        em = embed(f"> 퐁 {round(bot.latency*1000)}ms <","blue")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}핑"+hide+em)

@bot.command()
async def 주사위(ctx, maxv):
    if ctx.author.id == bot.user.id:    
        maxx = int(maxv) + 1
        com = random.randrange(1,maxx)
        em = embed(f"> 🎲 {com} <","green")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}주사위 {maxv}"+hide+em)
        
@bot.command()
async def 숨기기(ctx,*, message):
    if ctx.author.id == bot.user.id:    
        await ctx.message.delete()
        await ctx.send(hide+message)

@bot.command()
async def 서버복사(ctx):
    if ctx.author.id == bot.user.id:
        try:
            url = f"https://canary.discord.com/api/v8/guilds"
            headers = {"authorization": token}
            payload = {"name": ctx.guild.name}
            res = requests.post(url, headers=headers, json=payload)
            r = res.json()
            id = r['id']
            TOKEN = token
            COPY_GUILD = ctx.guild.id
            RESULT_GUILD = id 
            API_BASE = "https://discord.com/api/v9"
            def isRatelimit(obj):
                if obj.get("global", None) != None:
                    return True, obj.get("retry_after", 0.0)
                else:
                    return False, 0
            headers = {"authorization": TOKEN}
            result_channels = requests.get(f"{API_BASE}/guilds/{RESULT_GUILD}/channels", headers=headers).json()
            result_roles = requests.get(f"{API_BASE}/guilds/{RESULT_GUILD}/roles", headers=headers).json()
            for channel in result_channels:
                while True:
                    delete_channel = requests.delete(f"{API_BASE}/channels/{channel['id']}", headers=headers).json()
                    ratelimit, sleep = isRatelimit(delete_channel)
                    if ratelimit:
                        time.sleep(sleep)
                    else:
                        break
            for channel in result_roles:
                while True:
                    delete_channel = requests.delete(f"{API_BASE}/guilds/{RESULT_GUILD}/roles/{channel['id']}", headers=headers)
                    try:
                        delete_channel = delete_channel.json()
                    except:
                        delete_channel = {}
                    ratelimit, sleep = isRatelimit(delete_channel)
                    if ratelimit:
                        time.sleep(sleep)
                    else:
                        break
            original_channels = requests.get(f"{API_BASE}/guilds/{COPY_GUILD}/channels", headers=headers).json()
            original_roles = requests.get(f"{API_BASE}/guilds/{COPY_GUILD}/roles", headers=headers).json()
            original_guild = requests.get(f"{API_BASE}/guilds/{COPY_GUILD}", headers=headers).json()
            system_channel = original_guild.get("system_channel_id")
            if system_channel == None:
                system_channel = 0
            new_system_channel = 0
            category_channels = []
            channels = []
            for channel in original_channels:
                if channel["type"] == 4:
                    category_channels.append(channel)
                else:
                    channels.append(channel)
            original_roles.sort(key=lambda x: x["position"], reverse=True)
            for role in original_roles:
                while True:
                    if role["managed"]:
                        break
                    if int(role["id"]) == int(COPY_GUILD):
                        for i in range(len(channels)):
                            par = channels[i].get("permission_overwrites")
                            if par:
                                for j in range(len(par)):
                                    if par[j]["id"] == role["id"]:
                                        channels[i]["permission_overwrites"][j]["id"] = RESULT_GUILD
                        break
                    obj = role
                    create_role = requests.post(f"{API_BASE}/guilds/{RESULT_GUILD}/roles", json=obj, headers=headers).json()
                    ratelimit, sleep = isRatelimit(create_role)
                    if ratelimit:
                        time.sleep(sleep)
                    else:
                        for i in range(len(channels)):
                            par = channels[i].get("permission_overwrites")
                            if par:
                                for j in range(len(par)):
                                    if par[j]["id"] == role["id"]:
                                        channels[i]["permission_overwrites"][j]['id'] = create_role['id']
                        for i in range(len(category_channels)):
                            par = category_channels[i].get("permission_overwrites")
                            if par:
                                for j in range(len(par)):
                                    if par[j]["id"] == role["id"]:
                                        category_channels[i]["permission_overwrites"][j]["id"] = create_role["id"]
                        break
            for category in category_channels:
                while True:
                    obj = category
                    del obj["guild_id"]
                    create_channel = requests.post(f"{API_BASE}/guilds/{RESULT_GUILD}/channels", json=obj,
                                                headers=headers).json()
                    ratelimit, sleep = isRatelimit(create_channel)
                    if ratelimit:
                        time.sleep(sleep)
                    else:
                        for i in range(len(channels)):
                            par = channels[i].get("parent_id")
                            if par:
                                if par == category["id"]:
                                    channels[i]["parent_id"] = create_channel["id"]
                        break
            for channel in channels:
                try:
                    while True:
                        obj = channel
                        del obj["guild_id"]

                        create_channel = requests.post(f"{API_BASE}/guilds/{RESULT_GUILD}/channels", json=obj,
                                                    headers=headers).json()
                        ratelimit, sleep = isRatelimit(create_channel)
                        if ratelimit:
                            time.sleep(sleep)
                        else:
                            if obj["id"] == system_channel:
                                new_system_channel = create_channel["id"]
                            break
                except:
                    pass
            res = requests.get(f"https://discordapp.com/api/v9/guilds/{RESULT_GUILD}", headers=headers).json()
            id = res['id']
            sv = bot.get_guild(int(id))
            em = embed(f"> 서버 복사 성공 <","green")
        except:
            em = embed(f"> 서버 복사에 실패함 사유 : 몰라 <","red")
        await ctx.message.delete()
        await ctx.send(f"> {prefix}서버복사"+hide+em)

@bot.command()
async def 봇(ctx, *, rec):
    if ctx.author.id == bot.user.id:
        await ctx.message.delete()
        await ctx.send("https://discord.com/oauth2/authorize?client_id={rec}&permissions=8&scope=bot")

@bot.command()
async def 웹(ctx,*, link):
    if ctx.author.id == bot.user.id:
        await ctx.message.delete()
        await ctx.send(f"`{link}` "+hide+f"https://api.apiflash.com/v1/urltoimage?access_key=b52be4c6268c429bac8afd0bcf64a2f1&wait_until=page_loaded&url={link}")

bot.run(token, bot=False)
