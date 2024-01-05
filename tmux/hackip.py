import asyncio
import os
import random
import sys
from base64 import b64decode as kc
from time import sleep

import requests

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


def get_ipaddres_data(input):
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={input}"
    location_param = f"{location_link}://{location_api}/?{location_key}&{location_search}"
    response = requests.get(location_param)
    if response.status_code != 200:
        return "Sorry, there was an error processing your request. Please try again later"
    data_location = response.json()
    try:
        location_ip = data_location["ip"]
        location_code = data_location["country_code"]
        location_name = data_location["country_name"]
        location_region = data_location["region_name"]
        location_city = data_location["city_name"]
        location_zip = data_location["zip_code"]
        location_zone = data_location["time_zone"]
        location_card = data_location["as"]
    except Exception as e:
        return f"Error {e}"
    if (
        location_ip
        and location_code
        and location_name
        and location_region
        and location_city
        and location_zip
        and location_zone
        and location_card
    ):
        location_target = ""
        location_target += f"IP Address: {location_ip}\n"
        location_target += f"Country code: {location_code}\n"
        location_target += f"Country name: {location_name}\n"
        location_target += f"Region name: {location_region}\n"
        location_target += f"City name: {location_city}\n"
        location_target += f"Zip code: {location_zip}\n"
        location_target += f"Time Zone: {location_zone}\n"
        location_target += f"Data card: {location_card}\n"
        return location_target
    else:
        return "Not data ip address"


async def now_tracking():
    os.system("clear")
    try:
        import requests
    except ImportError:
        print("Requests library not found. Installing...")
        return
    print
    Loading("" + Yellow + "Loading........")
    print
    print
    Developed()
    print
    sleep(2)
    ipaddress = input("" + White + "You enter the tracking IP: ")
    hack = get_ipaddres_data(ipaddress)
    try:
        print
        Loading("" + Yellow + "Now tracking loading.......")
        print
        sleep(3)
        print
        Loading("" + Yellow + f"{hack}\n")
        print
    except:
        print("fixed connection")


if __name__ == "__main__":
    asyncio.run(now_tracking())
