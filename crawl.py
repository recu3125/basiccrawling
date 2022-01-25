from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup
import re
import os
import time


def clearConsole():
    command = 'cls'
    os.system(command)


url = ''
selector = ''


clearConsole()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
resultlist = []
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)


def F(url):
    wordlist = []
    global resultlist
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one(
            selector)
        clearConsole()
        print(str(i)+'/'+str(loopval))
        wordlist = list(filter(lambda x: len(x) <= 6, wordlist))
        resultlist = list(dict.fromkeys(resultlist + wordlist))
    else:
        print('a')


loopval = 1000
for i in range(1, loopval):
    try:
        F()
    except:
        print("error, waiting 5s")
        time.sleep(5)

with open('out.txt', 'w', encoding='utf8') as f:
    for item in resultlist:
        f.write("%s\n" % item)
