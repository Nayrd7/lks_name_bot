import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='пинг', description="Пингует участника в ответ для проверки работоспособности бота")
    async def ping(
            self,
            interaction,
            pick: str = commands.Param(
                name='эфемерное',
                description='Показать сообщение только вам?',
                choices=['Да', 'Нет']
            ),
    ):
        embed = disnake.Embed(
            color=0x00ff00
        )
        if pick.lower() == 'да':
            pick = True
            embed.add_field(
                name='Понг!',
                value='Вы включили эфемерное сообщение.',
                inline=False
            )
        else:
            pick = False
            embed.add_field(
                name='Понг!',
                value='Вы отключили эфемерное сообщение.',
                inline=False
            )

        await interaction.response.send_message(embed=embed, ephemeral=pick)


def setup(bot):
    bot.add_cog(Ping(bot))
