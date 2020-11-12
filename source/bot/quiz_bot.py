from discord.ext import commands

from bot.context import Context
from models.quiz import Quiz
from settings import ROLES_ORGANIZER, EMOJI_DECLINE, EMOJI_OK
from util.text import *
from bot.server_management import ServerManagement


class QuizBot(commands.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._guild = None
        self._management = None
        self._quiz_message = None
        self._quiz = None
        self._participants = set()

        bot.add_cog(self)

    # Private

    async def _setup(self):
        # Create organization category or get the existing handle
        organization = await self._management.get_or_create_category(text(CHANNEL_ORGA))
        await self._management.get_or_create_text_channel(text(CHANNEL_LOBBY), organization)
        await self._management.get_or_create_voice_channel(text(CHANNEL_LOBBY), organization)
        await self._management.get_or_create_text_channel(text(CHANNEL_SETUP), organization)

    async def _tear_down(self):
        pass

    # Public

    def exit(self):
        pass

    def participant_text(self):
        return ', '.join(map(str, self._participants))

    # Commands and listeners

    @commands.Cog.listener()
    async def on_ready(self):
        self._guild = self._bot.guilds[0]
        self._management = ServerManagement(self._bot, self._guild)

        await self._setup()

    @commands.Cog.listener()
    async def on_disconnect(self):
        await self._tear_down()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if isinstance(error, commands.errors.CheckFailure):
        #     await ctx.message.author.send(text(WRONG_ROLE))
        print(error)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id == self._quiz_message.id:

            # Stop the quiz (only if an organizer says so).
            if reaction.emoji == EMOJI_DECLINE and Context.has_any_role(None, user, ROLES_ORGANIZER):
                await self._quiz_message.delete()
                self._quiz_message = None

            # Add a new participant.
            elif reaction.emoji == EMOJI_OK:
                self._participants.add(Context.get_nick_or_name(None, user))
                await self._quiz_message.edit(content=text(NEW_QUIZ).format(self._quiz.type, self.participant_text()))

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.id == self._quiz_message:
            # Remove a participant.
            if reaction.emoji == EMOJI_OK:
                pass

    @commands.command(name='quiz',
                      aliases=['newquiz, organize'],
                      help='Schedules a new quiz')
    @commands.has_any_role(*ROLES_ORGANIZER)
    async def organize(self, ctx, quiz_type: str = None, team_size: str = None):
        if quiz_type not in ['normal', 'jeopardy', 'only connect']:
            quiz_type = 'normal'

        self._quiz = Quiz(quiz_type)

        await ctx.message.delete()
        self._quiz_message = await ctx.send(text(NEW_QUIZ).format(quiz_type, self.participant_text()))
