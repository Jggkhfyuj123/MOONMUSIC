from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝗔∂∂ 𝗠є 𝗬συя 𝗚яσυρ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✫𝐅𝐄𝐀𝐓𝐔𝐑𝐄✫",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✫𝐒𝐄𝐓𝐓𝐈𝐍𝐆✫", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝗔∂∂ 𝗠є 𝗬συя 𝗚яσυρ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="✫𝗢𝗪𝗡𝗘𝗥✫", url=f"https://t.me/IND_K4K4SHI",
            ),
        
            InlineKeyboardButton(
                text="✩𝐆𝐫𝐨𝐮𝐩☆", url=f"https://t.me/+An4yRwJGNq5mZWFl",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✫𝗖𝗢𝗠𝗠𝗔𝗠𝗗𝗦✫", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
