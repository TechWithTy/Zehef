from bs4 import BeautifulSoup
from ...lib.Requests import Request
from ...lib.colors import *

def pornhub(target: str):
    try:
        s = Request(url=None).Session()

        r = s.get("https://fr.pornhub.com/signup")

        soup = BeautifulSoup(r.text, 'html.parser')
        token = soup.find(attrs={'name': 'token'}).get('value')

        params = {'token': token}
        data = {'check_what': 'email', 'email': target}

        api = s.post(f"https://fr.pornhub.com/user/create_account_check", params=params, data=data)
        s.close()

        if api.json()['email'] == "create_account_passed":
            print(f"{RED}>{WHITE} Pornhub")
            return False
        elif api.json()['email'] == "create_account_failed":
            print(f"{GREEN}>{WHITE} Pornhub")
            return True
        else:
            print(f"{RED}>{WHITE} Pornhub")
            return False

    except:
        s.close()
        return None