import os
from dotenv import load_dotenv
import discord as dc

load_dotenv()
bot_token = os.getenv("bot_token")

from api.make_request import MakeRequest
from commands.weather import Weather

bot = dc.Bot()

@bot.event
async def on_ready():
    print(f"Bott has logged in as: {bot.user}")

@bot.slash_command(name="hi")
async def hi(ctx):
    await ctx.respond("Hello")

@bot.slash_command(name="ping")
async def ping(ctx, url: str):
    request = MakeRequest(url)
    request = request.make_request()
    print(request)
    request = request.text
    return await ctx.respond(f"Pinged {url} with response: {request}")

@bot.slash_command(name="weather")
async def weather(ctx, city: str):
    data = Weather.get_weather(city, MakeRequest)
    return await ctx.respond(f"Temperature in {city} at {data['current_weather']['time']}: {data['current_weather']['temperature']}°C, Wind Speed: {data['current_weather']['windspeed']} km/h")
    

if __name__ == "__main__":
    bot.run(bot_token)