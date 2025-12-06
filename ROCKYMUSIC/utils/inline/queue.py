# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @mrRockytg
# ===========================================================

from typing import Union
from ROCKYMUSIC import app
from ROCKYMUSIC.utils.formatters import time_to_seconds
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


#def aq_markup(_, chat_id):
   # buttons = [
       # [
           # InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
         #   InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
           # InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
           # InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
           # InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
      #  ],
       # [
          #  InlineKeyboardButton(
              #  text="˹ᴄʜᴀᴛ ʙᴏᴛ˼ ", url=f"https://t.me/JullyChatBot"
             #),
          #  InlineKeyboardButton(
              #  text="˹ᴍᴜsɪᴄ ʙᴏᴛ ˼", url=f"https://t.me/ShriramxBot"
            #),
        #],
     # ]
    #return buttons

def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴄʜᴀᴛ ʙᴏᴛ •",
                url=f"https://t.me/JullyChatBot"
            ),
            InlineKeyboardButton(
                text="• ᴍᴜsɪᴄ ʙᴏᴛ •",
                url="https://t.me/ShriramxBot"
            ),
        ],
    ]
    return buttons

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/mrrockytg
# 🔗 Source link : t.me/rockyxsupport
# 📢 Telegram channel : t.me/rockyxupdate
# ===========================================================
