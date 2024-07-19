from ...lib.Requests import Request
from ...lib.colors import *


async def instagram(target: str):
    # Step 1: Verify Request to Instagram's Signup Page
    req = await Request("https://www.instagram.com/accounts/emailsignup/").get()

    # Step 2: Retrieve and Validate Cookies
    try:
        csrf_token = req.cookies.get('csrftoken')
    except:
        print(f"{RED}>{WHITE} Instagram / Csrftoken not found")
        pass


    # Prepare data for the next request
    data = {
        'email': target,
        'first_name': '',
        'username': '',
        'opt_into_one_tap': False
    }

    # Step 3: Make the post request with the csrf_token
    r = await Request("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers={'x-csrftoken': csrf_token}, data=data).post()

    # Step 4: Handle response and possible errors
    try:
        code = r.json().get('errors', {}).get('email', [{}])[0].get('code')

        if code == 'email_is_taken':
            print(f"{GREEN}>{WHITE} Instagram")
            return True
        else:
            print(f"{RED}>{WHITE} Instagram")
            return False
    except (KeyError, IndexError) as e:
        print(f"{RED}>{WHITE} Instagram error: {str(e)}")
        return None
    except Exception as e:
        print(f"{RED}>{WHITE} Error: {str(e)}")
        return None