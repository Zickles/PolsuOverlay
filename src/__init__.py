"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                                                      ┃
┃                                                  Polsu's Overlay                                                     ┃
┃                                                                                                                      ┃
┃                                                                                                                      ┃
┃  • A Hypixel Bedwars Overlay in Python, 100% free and open source!                                                   ┃
┃  > https://github.com/Polsu-Development/PolsuOverlay                                                                 ┃
┃  • Made by Polsu's Development Team                                                                                  ┃
┃                                                                                                                      ┃
┃                                                                                                                      ┃
┃                                                                                                                      ┃
┃                               © 2023 - 2024, Polsu Development - All rights reserved                                 ┃
┃                                                                                                                      ┃
┃  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the    ┃
┃  following conditions are met:                                                                                       ┃
┃                                                                                                                      ┃
┃  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the           ┃
┃     following disclaimer.                                                                                            ┃
┃                                                                                                                      ┃
┃  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the        ┃
┃     following disclaimer in the documentation and/or other materials provided with the distribution.                 ┃
┃                                                                                                                      ┃
┃  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,  ┃
┃  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE   ┃
┃  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,  ┃
┃  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR     ┃
┃  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,   ┃
┃  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE    ┃
┃  USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                            ┃
┃                                                                                                                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

# DO NOT EDIT THIS FILE PLEASE, THIS MIGHT LEAD TO SOME FUNCTIONALITIES NOT WORKING


from os import getcwd, environ, name
from dotenv import load_dotenv

__title__ = "PolsuOverlay"
__author__ = "Polsulpicien"
__license__ = "GPL-3.0 License"
__version__ = "2.0.7"
__description__ = "Polsu's Overlay"

__module__ = getcwd()

__header__ = {
    "User-Agent": f"Polsu Overlay - v{__version__}"
}

# Check if the module is executable or not
if not __module__.endswith("PolsuOverlay"):
    __module__ = __module__ + "/"
    EXECUTABLE = True
else:
    __module__ = __module__
    EXECUTABLE = False

LINUX = True if name == 'posix' else False


load_dotenv('.env')

DEV_MODE = True if environ.get("DEV_MODE", "False") == "True" else False


# This will only change the local cache, not the API cache
#
# - Lower this value and you will make more requests to the API
# - Higher this value and you will make less requests to the API
#
# WARNING: Setting this value lower will only make your Overlay slower!
CACHE = 1200


from .PolsuAPI import Polsu

from .components.rpc import Presence
from .components.notifications import Notif
from .components.table import Table
from .components.menu import Menu
from .components.apikey import APIKeyMenu, openSettings
from .components.reward import Rewards
from .components.logs import Logs
from .components.player import Player
from .components.settings import Settings

from .utils.text import text2html
from .utils.skin import SkinIcon
from .utils.themes import loadThemes
