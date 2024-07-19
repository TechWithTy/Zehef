from ...lib.Requests import Request
from ...lib.colors import *

async def github(target: str):

    r = await Request(f"https://api.github.com/search/users?q={target}+in:email").get()

    try:
        if '"total_count": 0' in r.text:
            print(f"{RED}>{WHITE} Github")
            return False
        else:
            try:
                print(f"{GREEN}>{WHITE} Github ~ Name : {r.json()['items'][0]['login']}")
                return True
            except:
                print(f"{RED}>{WHITE} Github")
                return False
    except:
        return None