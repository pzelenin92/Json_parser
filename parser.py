"""This script extracts email corresponding to given ip address. To run this script in console type:
python parser.py ip_address name_of_json.json"""
import json
import sys

ip = sys.argv[1]
name_json = sys.argv[2]
OUTPUT_EMAIL = False

with open(name_json, "r") as input_json:
    data = json.load(input_json)
    for key in data["list"]:
        for ip4_keys in key["ip4"]:
            if ip4_keys["ip"] == ip:
                OUTPUT_EMAIL = key["account"]["email"]
    if OUTPUT_EMAIL:
        print(OUTPUT_EMAIL)
    else:
        print("There is no such ip here")
