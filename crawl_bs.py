import requests
from bs4 import BeautifulSoup
import re
import os
import time
import math
import xml.etree.ElementTree as ET


def clearConsole():
  command = 'cls'
  os.system(command)


url = ''
selector = ''

start = int(input())*100000+1

clearConsole()
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
resultlist = []
requests.packages.urllib3.disable_warnings(
  requests.packages.urllib3.exceptions.InsecureRequestWarning)

def F():
  global resultlist
  wordlist = []
  response = requests.get('', headers=headers, verify=False)
  if response.status_code == 200:
    xml = response.text
    lyric = ET.fromstring(xml).find("result").find("trackInformation").find("lyric").text
    lyric = str(lyric).replace('<br>',' ').replace('<br/>',' ').replace('<p>',' ').replace('</p>',' ').replace('<div>',' ').replace('</div>',' ')
    lyric = re.sub('[\'\"\]\[!#$%&’\(\)\*\+,\.\/:;<=>\?@\\\\^_`\{\|\}~\-]'," ",lyric)

    if re.fullmatch(".*[^ 가-힣a-zA-Z0-9\'\"\]\[!#$%&’\(\)\*\+,\.\/:;<=>\?@\\\\^_`\{\|\}~\-].*",lyric)!=None:
      pass
    else:
      wordlist=str(lyric).split(' ')
      wordlist = list(filter(lambda x: len(x) <= 6 and len(x) >= 2 and re.fullmatch('[가-힣]*',x)!=None, wordlist))
      resultlist = resultlist + list(dict.fromkeys(wordlist))
  else:
    print('a')


starttime = round(time.time())
loopval = 56323120
for i in range(0,len(idlist)):
  clearConsole()
  print(len(idlist))
  print(i)
  try:
    F()
  except:
    print("nolyr")


with open('hiphop.txt', 'w', encoding='utf8') as f:
  resultlist = list(dict.fromkeys(resultlist))
  for item in resultlist:
    f.write("%s\n" % item)