"""
Copyright (c) 2019-2023 The RyuzakiLib @xtdevs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio
import os


def runner_up():
    os.system(
        "pip3 install -r req* && python3 setup.py build && python3 setup.py install && python3 setup.py upload"
    )


def user_gmail_and_username(user_gmail: str = None, user_username: str = "TeamKillerX"):
    os.system(f"git config --global user.email '{user_gmail}'")
    os.system(f"git config --global user.username '{user_username}'")


async def setting_github():
    user_gmail = input("enter your gmail: ")
    try:
        user_gmail_and_username(user_gmail)
    except Exception as e:
        print(str(e))
        return
    # runner_up()


if __name__ == "__main__":
    asyncio.run(setting_github())
