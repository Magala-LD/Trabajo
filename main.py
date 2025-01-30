import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('--- Conexión exitosa con Discord ---')

    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            # Borra el mensaje con el comando
            await message.delete()

            # Envía el mensaje que se borrará después de 3 segundos
            msg = await message.channel.send('[este mensaje se borrara]', delete_after=3.0)


    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')
