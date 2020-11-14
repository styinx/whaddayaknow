import discord
from discord.ext import commands

from bot.context import Context
from bot.server_management import ServerManagement
from models.quiz import Quiz
from models.team import Team
from settings import *
from util.text import *


class QuizBot(commands.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._guild = None
        self._management = None

        self._quiz_message = None
        self._quiz = None

        bot.add_cog(self)

    # Private

    async def _setup(self):
        # Create organization category or get the existing handle
        organization = await self._management.get_or_create_category(text(CHANNEL_CATEGORY))
        await self._management.get_or_create_text_channel(text(CHANNEL_LOBBY), organization)
        await self._management.get_or_create_voice_channel(text(CHANNEL_LOBBY), organization)
        await self._management.get_or_create_text_channel(text(CHANNEL_SETUP), organization)

        # Create roles
        await self._management.get_or_create_role(text(QUIZ_MASTER), discord.Colour(COLOR_QUIZ_MASTER))

    async def _tear_down(self):
        pass

    # Public

    def exit(self):
        pass

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
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.message.author.send('Oops something went wrong!' + str(error))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id != self._quiz_message.id:
            return

        # Organizer reactions
        if Context.has_any_role(None, user, ROLES_ORGANIZER):
            # Start the quiz.
            if reaction.emoji == EMOJI_ACCEPT:
                await self._quiz_message.delete()
                self._quiz_message = None
            # Stop the quiz.
            elif reaction.emoji == EMOJI_DECLINE:
                await self._quiz_message.delete()
                self._quiz_message = None

        # Quiz master reactions
        if user == self._quiz.master:
            # Next question
            if reaction.emoji == EMOJI_FORWARD:
                pass

            # Next question
            elif reaction.emoji == EMOJI_BACKWARD:
                pass

            # Pause or restart timer
            elif reaction.emoji == EMOJI_PLAY_PAUSE:
                pass

        # Anyone else
        else:
            # Add a new participant.
            if reaction.emoji == EMOJI_OK:
                self._quiz.add_participant(user)
                await self._quiz_message.edit(content=self._quiz.organization_text())

            # Join team
            elif reaction.emoji in EMOJI_TEAM:
                pass

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.id == self._quiz_message:
            # Remove a participant.
            if reaction.emoji == EMOJI_OK:
                self._quiz.remove_participant(user)
                await self._quiz_message.edit(content=self._quiz.organization_text())

            # Leave team
            elif reaction.emoji in EMOJI_TEAM:
                pass

    @commands.command(name='quiz',
                      aliases=['newquiz, organize'],
                      help='Schedules a new quiz')
    @commands.has_any_role(*ROLES_ORGANIZER)
    async def organize(self, ctx, quiz_type: str = None, team_size: str = None):
        if ctx.channel.name != text(CHANNEL_SETUP):
            return

        if quiz_type not in ['normal', 'jeopardy', 'only connect']:
            quiz_type = 'normal'

        if not team_size:
            team_size = 2

        team_size = min(max(int(team_size), 2), 8)

        self._quiz = Quiz(quiz_type, ctx.message.author, team_size)
        self._quiz_message = await ctx.send(self._quiz.organization_text())

        await self._quiz_message.add_reaction(EMOJI_OK)
        await self._quiz_message.add_reaction(EMOJI_ACCEPT)
        await self._quiz_message.add_reaction(EMOJI_DECLINE)

        try:
            for team_id in range(1, team_size + 1):
                role = await self._management.get_or_create_role('Team ' + str(team_id))
                team = Team(role, team_id)
                self._quiz.add_team(team)
                await self._quiz_message.add_reaction(EMOJI_TEAM[team_id - 1])
        except Exception as e:
            print(e)

        await ctx.message.delete()
