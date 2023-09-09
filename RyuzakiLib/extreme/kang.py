import asyncio
from PIL import Image, ImageDraw, ImageFont
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

class KangingSticker:
    def __init__(self, args):
        self.args = args
        
    async def kang_take_sticker(self, client: Client, message: Message):
        user = client.me
        replied = message.reply_to_message
        um = await message.edit_text("`Trying to kang...`")
        media_ = None
        emoji_ = None
        is_anim = False
        is_video = False
        resize = False
        ff_vid = False
        if replied and replied.media:
            if replied.photo:
                resize = True
            elif replied.document and "image" in replied.document.mime_type:
                resize = True
                replied.document.file_name
            elif replied.document and "tgsticker" in replied.document.mime_type:
                is_anim = True
                replied.document.file_name
            elif replied.document and "video" in replied.document.mime_type:
                resize = True
                is_video = True
                ff_vid = True
            elif replied.animation:
                resize = True
                is_video = True
                ff_vid = True
            elif replied.video:
                resize = True
                is_video = True
                ff_vid = True
            elif replied.sticker:
                if not replied.sticker.file_name:
                    await um.edit("**The sticker has no Name!**")
                    return
                emoji_ = replied.sticker.emoji
                is_anim = replied.sticker.is_animated
                is_video = replied.sticker.is_video
                if not (
                    replied.sticker.file_name.endswith(".tgs")
                    or replied.sticker.file_name.endswith(".webm")
                ):
                    resize = True
                    ff_vid = True
            else:
                await um.edit("**Unsupported Files**")
                return
            media_ = await client.download_media(replied, file_name="resources/")
        else:
            await um.edit("**Please Reply to Photo/GIF/Sticker Media!**")
            return
        if media_:
            args = self.args
            pack = 1
            if len(args) == 2:
                emoji_, pack = args
            elif len(args) == 1:
                if args[0].isnumeric():
                    pack = int(args[0])
                else:
                    emoji_ = args[0]
            if emoji_ and emoji_ not in (
                getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
            ):
                emoji_ = None
            if not emoji_:
                emoji_ = "🗿"
                
            u_name = user.username
            u_name = "@" + u_name if u_name else user.first_name or user.id
            packname = f"Sticker_u{user.id}_v{pack}"
            custom_packnick = f"{client.me.first_name} by {u_name}"
            packnick = f"{custom_packnick} Vol.{pack}"
            cmd = "/newpack"
            if resize:
                media_ = await resize_media(media_, is_video, ff_vid)
            if is_anim:
                packname += "_animated"
                packnick += " (Animated)"
                cmd = "/newanimated"
            if is_video:
                packname += "_video"
                packnick += " (Video)"
                cmd = "/newvideo"
            exist = False
            while True:
                try:
                    exist = await client.invoke(
                        GetStickerSet(
                            stickerset=InputStickerSetShortName(short_name=packname), hash=0
                        )
                    )
                except StickersetInvalid:
                    exist = False
                    break
                limit = 50 if (is_video or is_anim) else 120
                if exist.set.count >= limit:
                    pack += 1
                    packname = f"a{user.id}_by_userge_{pack}"
                    packnick = f"{custom_packnick} Vol.{pack}"
                    if is_anim:
                        packname += f"_anim{pack}"
                        packnick += f" (Animated){pack}"
                    if is_video:
                        packname += f"_video{pack}"
                        packnick += f" (Video){pack}"
                    await um.edit(
                        f"`Create a New Sticker Pack {pack} Because the Sticker Pack Is Full`"
                    )
                    continue
                break
            if exist is not False:
                try:
                    await client.send_message("stickers", "/addsticker")
                except YouBlockedUser:
                    await client.unblock_user("stickers")
                    await client.send_message("stickers", "/addsticker")
                except Exception as e:
                    return await um.edit(f"**ERROR:** `{e}`")
                await asyncio.sleep(2)
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                limit = "50" if is_anim else "120"
                while limit in await get_response(message, client):
                    pack += 1
                    packname = f"a{user.id}_by_{user.username}_{pack}"
                    packnick = f"{custom_packnick} vol.{pack}"
                    if is_anim:
                        packname += "_anim"
                        packnick += " (Animated)"
                    if is_video:
                        packname += "_video"
                        packnick += " (Video)"
                    await um.edit(
                        "`Create a New Sticker Pack "
                        + str(pack)
                        + " Because the sticker pack is full`"
                    )
                    await client.send_message("stickers", packname)
                    await asyncio.sleep(2)
                    if await get_response(message, client) == "Invalid pack selected.":
                        await client.send_message("stickers", cmd)
                        await asyncio.sleep(2)
                        await client.send_message("stickers", packnick)
                        await asyncio.sleep(2)
                        await client.send_document("stickers", media_)
                        await asyncio.sleep(2)
                        await client.send_message("Stickers", emoji_)
                        await asyncio.sleep(2)
                        await client.send_message("Stickers", "/publish")
                        await asyncio.sleep(2)
                        if is_anim:
                            await client.send_message(
                                "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                            )
                            await asyncio.sleep(2)
                        await client.send_message("Stickers", "/skip")
                        await asyncio.sleep(2)
                        await client.send_message("Stickers", packname)
                        await asyncio.sleep(2)
                        await um.edit(
                            f"**Sticker Added Successfully!**\n         **[CLICK HERE](https://t.me/addstickers/{packname})**\n**To Use Stickers**"
                        )
                        return
                await client.send_document("stickers", media_)
                await asyncio.sleep(2)
                if (
                    await get_response(message, client)
                    == "Sorry, the file type is invalid."
                ):
                    await um.edit(
                        "**Failed to Add Sticker, Use @Stickers Bot To Add Your Sticker.**"
                    )
                    return
                await client.send_message("Stickers", emoji_)
                await asyncio.sleep(2)
                await client.send_message("Stickers", "/done")
            else:
                await um.edit("`Create a New Sticker Pack`")
                try:
                    await client.send_message("Stickers", cmd)
                except YouBlockedUser:
                    await client.unblock_user("stickers")
                    await client.send_message("stickers", "/addsticker")
                await asyncio.sleep(2)
                await client.send_message("Stickers", packnick)
                await asyncio.sleep(2)
                await client.send_document("stickers", media_)
                await asyncio.sleep(2)
                if (
                    await get_response(message, client)
                    == "Sorry, the file type is invalid."
                ):
                    await um.edit(
                        "**Failed to Add Sticker, Use @Stickers Bot To Add Your Sticker.**"
                    )
                    return
                await client.send_message("Stickers", emoji_)
                await asyncio.sleep(2)
                await client.send_message("Stickers", "/publish")
                await asyncio.sleep(2)
                if is_anim:
                    await client.send_message("Stickers", f"<{packnick}>")
                    await asyncio.sleep(2)
                await client.send_message("Stickers", "/skip")
                await asyncio.sleep(2)
                await client.send_message("Stickers", packname)
                await asyncio.sleep(2)
            await um.edit(
                f"**Sticker Added Successfully!**\n         **[CLICK HERE](https://t.me/addstickers/{packname})**"
            )
            if os.path.exists(str(media_)):
                os.remove(media_)

async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text
