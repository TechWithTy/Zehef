from ...lib.colors import *
from ...lib.Requests import Request

async def x(target: str):

    r = await Request(f"https://api.twitter.com/i/users/email_available.json?email={target}").get()

    try:
        if r.json()['taken']:
            print(f"{GREEN}>{WHITE} 𝕏")
            return True
        else:
            print(f"{RED}>{WHITE} 𝕏")
            return False
    except:
        print(f"{RED}>{WHITE} 𝕏")
        return None