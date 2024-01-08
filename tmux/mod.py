import asyncio
import os
import random
import sys
from time import sleep

Red = "\33[0;31m"
Green = "\33[0;32m"
Yellow = "\33[0;33m"
Purple = "\33[0;34m"
Pink = "\33[0;35m"
Cyan = "\33[0;36m"
White = "\33[0;37m"
Normal = "\33[0m"


def Loading(text):
    for x in text + "\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(random.random() * 0.05)


def Developed():
    Loading(
        ""
        + Yellow
        + """
Github : TeamKillerX
Developer: t.me/xtdevs
Hacking : tools all
"""
    )


def install_termux_required():
    os.system(
        "pkg update -y && pkg upgrade -y && pkg install python-pip -y && pkg install git curl wget python3 -y && pkg install nodejs -y"
    )


def uninstall_ryuzakilib():
    full_install = "git clone https://github.com/TeamKillerX/RyuzakiLib && cd RyuzakiLib && mv *src $HOME && cd ~ && rm -rf RyuzakiLib mod.py && cd src && npm install grammy axios && export DEBUG='grammy*'"
    os.system(full_install)


async def now_running_up():
    os.system("clear")
    print
    Developed()
    print
    print
    Loading("" + Yellow + "Installing Termux First")
    print
    install_termux_required()
    sleep(3)
    print
    Loading("" + Yellow + "Uninstall RyuzakiLib Loading.....")
    print
    uninstall_ryuzakilib()
    sleep(2)
    print
    Loading("" + Yellow + "Now Installing Done")
    print
    print
    Loading("" + Yellow + "You can type cd src && nano mod.js")
    print
    print
    Loading("" + Yello + "Your bot token here")
    print


if __name__ == "__main__":
    asyncio.run(now_running_up())
