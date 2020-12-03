
import bs4

import time

import requests

import keyboard
link = "https://www.google.com/search?client=opera-gx&q=доллар+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.441"}

page = requests.get(link, headers)

soup = bs4.BeautifulSoup(page.content, "html.parser")

def check_the_dollar_to_ruble():

                da_number = soup.findAll("div", {"class": "BNeawe iBp4i AP7Wnd"})

                ruble = da_number[1].text

                print("Сейчас 1 доллар стоит", ruble, sep=' ')


while True:
    if keyboard.is_pressed("shift"):
        break
    else:
        check_the_dollar_to_ruble()

        time.sleep(5)