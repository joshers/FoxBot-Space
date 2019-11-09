from redbot.core import commands

"""import launchlibrary as ll"""
import asyncio
import discord
import urllib.request
import json 

class FoxSpace(commands.Cog):
    """FoxSpace Commands"""

    @commands.command()
    async def nextlaunch(self, ctx):
        """Displays Next Rocket Launch from LaunchLibrary API"""
        """api = ll.Api(retries=10)     
        next_launch = ll.Launch.next(api, 1)
        launch_loc = next_launch[0].location
        launch_start = next_launch[0].windowstart
        launch_end = next_launch[0].windowend
        launch_name = next_launch[0].name
        launch_status = next_launch[0].status"""
        with urllib.request.urlopen("https://launchlibrary.net/1.4/launch/next/1") as url:
            launch = json.load(url.decode())
        launch_status = launch["status"]
        launch_start = launch["windowstart"]
        launch_end = launch["windowend"]
        launch_loc = launch["location"]
        launch_name = launch["name"]
        status = "Undetermined"
        color = 0x0000FF
        if launch_status == 1:
            status = "Green"
            color = 0x00FF00
        if launch_status == 2:
            status = "Red"
            color = 0xFF0000

        location = json.load(launch_loc)
        pad = json.load(location["pad"])
        padName = pad["name"]

        embed = discord.Embed(
            title="Next Launch", description=launch_name, color=color
        )
        embed.add_field(name="Status", value=status)
        embed.add_field(name="Window Begin", value=launch_start)
        embed.add_field(name="Window End", value=launch_end)
        embed.add_field(name="Pad", value=padName)

        await ctx.send(embed=embed)