import asyncio


"""
def __repr__(self):
    return "what ever needs to get stringereed"
    
e.g

str(Message.author) == chillfish#6621

"""


class CoolDownManager:
    def __init__(self, *args, **kwargs):
        self.cooldowns = []
        self._loop = asyncio.get_event_loop()

    def add_cooldown(self, cooldown: object):
        self.cooldowns.append(cooldown)

    async def check_instance(self, cooldown: str, return_list=False):
        """
        This is a check to see if a cool down exists in the list or not"""
        list_ = [str(x) for x in self.cooldowns]
        if cooldown in list_:
            r = 1
        else:
            r = -1
        if return_list:
            return r, list_
        else:
            return r

    async def remove_cooldown(self, cooldown: str):
        """ This is used to remove cool down objects """
        result, list_ = await self.check_instance(cooldown, return_list=True)
        if result:
            list_.remove(cooldown)
            return 1
        else:
            return -1

    async def remove_timeout(self, cooldown: str, identifier=None):
        """ This removes user cool downs if identifier is given or clears all if None """
        result, stringified_list = await self.check_instance(cooldown, return_list=True)
        if result:
            target_cooldown = self.cooldowns[stringified_list.index(cooldown)]
            if identifier is not None:  # Target a specific user
                await target_cooldown.clear_timeout(identifier)
            else:   # Target all users
                await target_cooldown.clear_all_timeouts()
        else:
            return -1

    async def is_on_cooldown(self, identifier, cooldown=None, check=False, return_time_left=False):
        """ This is the main function for checking users are on cool downs or not """
        if cooldown is not None:
            if check:
                result, stringified_list = await self.check_instance(cooldown=cooldown, return_list=True)
                if not result:
                    return -1

