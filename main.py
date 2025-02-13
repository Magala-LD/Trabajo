import discord
import random
from discord.ext import commands

# Configura el bot con el prefijo "!".
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de elementos que responderá el bot.
mi_lista = ["Desechos radiactivos Miles o millones de años", "Plástico (botellas, bolsas) 100 - 1,000 años", "Pilas y baterías Más de 1,000 años (y contaminan suelos y agua)", "Aluminio (latas de refresco) 200 - 500 años"]

tips = [
    "Usa transporte sostenible: Opta por caminar, usar la bicicleta o el transporte público en lugar de automóviles particulares para reducir las emisiones de CO₂.",
    "Ahorra energía: Apaga luces y electrodomésticos cuando no los uses, y elige bombillas de bajo consumo o LED para reducir la demanda de electricidad.",
    "Reduce, reutiliza y recicla: Disminuye el consumo de plásticos y otros materiales contaminantes, reutiliza lo que puedas y separa los residuos para facilitar el reciclaje.",
    "Consume productos ecológicos: Compra productos locales, orgánicos y con menos empaques para disminuir la contaminación generada por su producción y transporte.",
    "Evita el desperdicio de agua: Cierra los grifos mientras te cepillas los dientes, usa regaderas de bajo consumo y recolecta agua de lluvia para reducir el uso innecesario del agua potable."
]

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def lista(ctx):
    """Envía la lista como mensaje."""
    respuesta = "\n".join(mi_lista)
    await ctx.send(f"*Lista de elementos:*\n{respuesta}")

@bot.command()
async def tip(ctx):
    """Envía un tip aleatorio."""
    consejo = random.choice(tips)
    await ctx.send(f"💡 Tips para la reduccion de la contaminacion:* {consejo}")

# Ejecuta el bot con tu token
TOKEN = "-token-"
bot.run(TOKEN)
