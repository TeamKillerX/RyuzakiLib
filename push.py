import os
import asyncio

def runner_up():
    os.system("pip3 install -r req* && python3 setup.py build && python3 setup.py install && python3 setup.py upload")

async def setting_github():
    USER_GMAIL = input("you enter global config gmail from github: ")
    USER_USERNAME = input("you enter global config username from github: ")
    try:
        os.system(f"git config --global user.email '{USER_GMAIL}'")
        os.system(f"git config --global user.username '{USER_USERNAME}'")
    except:
        print("invalid github")
    runner_up()

asyncio.run(setting_github())
