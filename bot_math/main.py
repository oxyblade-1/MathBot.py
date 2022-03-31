import os
import discord
from discord.ext import commands
import json

f = open('config.json')

config = json.load(f)

bot = commands.Bot(command_prefix="&", description="Bot pour Réviser")

@bot.event
async def on_ready():
    print("___.           __                     __  .__     ")
    print("\\_ |__   _____/  |_     _____ _____ _/  |_|  |__  ")
    print(" | __ \\ /  _ \\   __\\   /     \\__  \\   __\\  |  \\")
    print(" | \\_\\ (  <_> )  |    |  Y Y  \\/ __ \\|  | |   Y  \\")
    print(" |___  /\\____/|__| /\\ |__|_|  (____  /__| |___|  /")
    print("     \\/            \\/       \\/     \\/          \\/")

    print("\nBot.Math is Ready! © by oxyblade")

#aller sur l'ent de stephane hesssel
@bot.command()
async def ent(ctx):
    embed = discord.Embed(title = "Acceder à l'ENT", color = 0x334FFF, description="[ENT Stephane_Hessel](https://stephane-hessel.mon-ent-occitanie.fr/)")
    embed.set_image(url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290041830")
    await ctx.send(embed = embed)

#automatismes
@bot.command()
async def auto(ctx):
    embed = discord.Embed(title = "Les Automatismes", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290170424",description="[video: Information chiffrée](https://www.youtube.com/watch?v=A9_qbI4GU14)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/758013590535143445/944666459844526192/Screenshot_2022-02-19_at_19-46-34_LE_COURS_La_derivation_-_Premiere.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Dérivée et Primitive
@bot.command()
async def deriv(ctx):
    embed = discord.Embed(title = "Les Dérivées | Primitives", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290173708",description="[video: Derivée](https://www.youtube.com/watch?v=A9_qbI4GU14)[ | Primitive](https://www.youtube.com/watch?v=05ikcAFcPZ0)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/758013590535143445/944659114724818954/prim_deriv.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

@bot.command()
async def prim(ctx):
    embed = discord.Embed(title = "Les Dérivées | Primitives", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290173708",description="[video: Derivée](https://www.youtube.com/watch?v=A9_qbI4GU14)[ | Primitive](https://www.youtube.com/watch?v=05ikcAFcPZ0)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/758013590535143445/944659114724818954/prim_deriv.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Suites
@bot.command()
async def suite(ctx):
    embed = discord.Embed(title = "Les Suites", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290181175",description="[video: Suites](https://www.youtube.com/watch?v=05UHsy9G4M4&)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/758013590535143445/944668305023701032/Screenshot_2022-02-19_at_19-54-09_ANALYSE_-_Concours_B_des_ENSA_-_Suites_arithmetiques_et_geometriques.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Fonction Inverses
@bot.command()
async def Finv(ctx):
    embed = discord.Embed(title = "Les Fonction Inverses", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290182915",description="[video: Fonction Inverse](https://www.youtube.com/watch?v=nzEdbdapkow)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/921436758695088159/944674871005282374/f_asymptote.PNG")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Fonction Exponentielle
@bot.command()
async def exp(ctx):
    embed = discord.Embed(title = "Les Fonction Exponentielle", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290187038",description="[video: Exponenetielle](https://www.youtube.com/watch?v=sCcy4IQKits)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/919369842916741224/944677840069201921/Screenshot_2022-02-19_at_19-54-09_ANALYSE_-_Concours_B_des_ENSA_-_Suites_arithmetiques_et_geometriques.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Equation Différentielle
@bot.command()
async def Edif(ctx):
    embed = discord.Embed(title = "Les Equations Différentielles", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290188319",description="[video: Diffrentielles](https://www.youtube.com/watch?v=qHF5kiDFkW8)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/919369842916741224/944679835513544845/Screenshot_2022-02-19_at_20-39-51_Equations_differentielles_lecon_parties_I-II-III_debut_pdf.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Logarithme Népérien
@bot.command()
async def Ln(ctx):
    embed = discord.Embed(title = "Les Equations Différentielles", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290191617",description="[video: Logarithme](https://www.youtube.com/watch?v=VJns0RfVWGg&)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/919369842916741224/944682018992717874/a03f7726c2e83f52e0a5cccbaf110bcd.jpg")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#Probabilitées Conditionnelles
@bot.command()
async def ProbaC(ctx):
    embed = discord.Embed(title = "Les Probabilitées Conditionnelles", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290192580",description="[video: Probabilitée](https://www.youtube.com/watch?v=5oBnmZVrOXE&list=PLVUDmbpupCapoStVETZ2x6iy0vCua0HvK)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/919369842916741224/944684224114479114/Screenshot_2022-02-19_at_20-56-42_probabilite_conditionnelle_Recherche_Google.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#nombre complexe
@bot.command()
async def complexe(ctx):
    embed = discord.Embed(title = "Nombre complexe (Forme Exponentielle)", url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290196413",description="[video: complexe](https://www.youtube.com/watch?v=ABo2m52oEYw)", color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/917117165839192164/958111270349979759/Sans_titre.png")
    embed.set_footer(text = "fin du cour !")
    await ctx.send(embed = embed)

#token bot
bot.run(config['token'])