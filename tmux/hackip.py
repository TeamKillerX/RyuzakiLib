import requests
import os
from time import sleep
from base64 import b64decode as kc
import asyncio

def get_ipaddres_data(input):
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={input}"
    location_param = (
        f"{location_link}://{location_api}/?{location_key}&{location_search}"
    )
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
        location_target += f"<b>IP Address:</b> {location_ip}\n"
        location_target += f"<b>Country code:</b> {location_code}\n"
        location_target += f"<b>Country name:</b> {location_name}\n"
        location_target += f"<b>Region name:</b> {location_region}\n"
        location_target += f"<b>City name:</b> {location_city}\n"
        location_target += f"<b>Zip code:</b> {location_zip}\n"
        location_target += f"<b>Time Zone:</b> {location_zone}\n"
        location_target += f"<b>Data card:</b> {location_card}\n"
        return location_target
    else:
        return "Not data ip address"

async def now_tracking():
    os.system("clear")
    print("Loading........")
    sleep(2)
    print("Hacker by @xtdevs")
    ipaddress = input("You enter the tracking IP: ")
    hack = get_ipaddres_data(ipaddress)
    try:
        print("Now tracking loading.......")
        sleep(3)
        print(f"{hack}\n")
    except:
        print("fixed connection")

asyncio.run(now_tracking())
