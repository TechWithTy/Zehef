from ...lib.Requests import Request
from ...lib.colors import *

async def strava(target: str):

    req = await Request(f"https://www.strava.com/athletes/email_unique?email={target}").get()

    try:
        if "false" in req.text:
            print(f"{GREEN}>{WHITE} Strava")
            return True
        elif "true" in req.text:
            print(f"{RED}>{WHITE} Strava")
            return False
        else:
            print(f"{RED}>{WHITE} Strava")
            return False
    except:
        return None