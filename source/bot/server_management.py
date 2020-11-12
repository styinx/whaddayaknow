def assemble(**kwargs):
    res = {}
    for k, v in kwargs.items():
        if v:
            res[k] = v
    return res


class ServerManagement:
    def __init__(self, bot, guild):
        self._bot = bot
        self._guild = guild

    # Channels

    async def create_category(self, name: str, permission=None):
        return await self._guild.create_category(**assemble(name=name, overwrites=permission))

    async def get_or_create_category(self, name: str, permission=None):
        for r in await self._guild.fetch_channels():
            if r.name == name:
                return r
        return await self.create_category(name, permission)

    async def create_text_channel(self, name: str, category=None, permission=None):
        return await self._guild.create_text_channel(**assemble(name=name, category=category, overwrites=permission))

    async def get_or_create_text_channel(self, name: str, category=None, permission=None):
        for r in await self._guild.fetch_channels():
            if r.name == name:
                return r
        return await self.create_text_channel(name, category, permission)

    async def create_voice_channel(self, name: str, category=None, permission=None):
        return await self._guild.create_voice_channel(**assemble(name=name, category=category, overwrites=permission))

    async def get_or_create_voice_channel(self, name: str, category=None, permission=None):
        for r in await self._guild.fetch_channels():
            if r.name == name:
                return r
        return await self.create_voice_channel(name, category, permission)

    # Roles

    async def create_role(self, name: str, color=None):
        return await self._guild.create_role(**assemble(name=name, color=color))

    async def get_or_create_role(self, name: str, color=None):
        for r in await self._guild.fetch_roles():
            if r.name == name:
                return r
        return await self._guild.create_role(name, color)
