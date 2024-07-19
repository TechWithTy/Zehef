import re
import asyncio

from .modules.accounts.twitter import x
from .modules.accounts.gravatar import gravatar
from .modules.accounts.spotify import spotify
from .modules.accounts.duolingo import duolingo
from .modules.accounts.pinterest import pinterest
from .modules.accounts.github import github
from .modules.accounts.strava import strava
from .modules.accounts.pornhub import pornhub
from .modules.accounts.chess import chess
from .modules.accounts.deezer import deezer
from .modules.accounts.imgur import imgur
from .modules.accounts.instagram import instagram
from .modules.breaches.pastedumper import Pastebin_Dumper


async def zehef_service(emails: list[str]):

    EMAIL_REGEX = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
    results = []
    for target in emails:
        if re.match(EMAIL_REGEX, target):
            chess_output = await chess(target)
            deezer_output = deezer(target)
            duolingo_output = await duolingo(target)
            github_output = await github(target)
            gravatar_output = await gravatar(target)
            imgur_output = imgur(target)
            instagram_output = await instagram(target)
            pinterest_output = await pinterest(target)
            pornhub_output = pornhub(target)
            spotify_output = await spotify(target)
            strava_output = await strava(target)
            x_output = await x(target)
            results.append({
                "chess": chess_output,
                "deezer": deezer_output,
                "duolingo": duolingo_output,
                "github": github_output,
                "gravatar": gravatar_output,
                "imgur": imgur_output,
                "instagram": instagram_output,
                "pinterest": pinterest_output,
                "pornhub": pornhub_output,
                "spotify": spotify_output,
                "strava": strava_output,
                "x": x_output
            })

        else:
            print("Invalid email format")
    return results