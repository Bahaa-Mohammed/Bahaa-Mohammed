from userge import filters

@userge.on_message(~filters.me & filters.private, group=-1)
async def pmblock(c, m):
      await m.from_user.block()
