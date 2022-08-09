from copyreg import constructor
from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import os
import time
import math


start = int(input())*10000+1

i=1
def clearConsole():
  command = 'cls'
  os.system(command)

clearConsole()
resultlist = []

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.image': 2})
driver = webdriver.Chrome("C:/Users/superhoy/Desktop/basiccrawling/chromedriver.exe", chrome_options=options)
driver.set_page_load_timeout(10)

def F():
  wordlist = []
  global resultlist
  driver.get(''+str(i))
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  lyric = soup.select_one('')
  lyric = str(lyric).replace('<br>',' ').replace('<br/>',' ').replace('<p>',' ').replace('</p>',' ').replace('<div>',' ').replace('</div>',' ')
  lyric = re.sub('[\'\"\]\[!#$%&’\(\)\*\+,\.\/:;<=>\?@\\\\^_`\{\|\}~\-]'," ",lyric)
  
  if re.fullmatch(".*[^ 가-힣a-zA-Z0-9\'\"\]\[!#$%&’\(\)\*\+,\.\/:;<=>\?@\\\\^_`\{\|\}~\-].*",lyric)!=None:
    pass
  else:
    wordlist=str(lyric).split(' ')
    wordlist = list(filter(lambda x: len(x) <= 6 and len(x) >= 2 and re.fullmatch('[가-힣]*',x)!=None, wordlist))
    resultlist = resultlist + list(dict.fromkeys(wordlist))
    collectedcnt+=1
starttime = round(time.time())
loopval = 56323120
collectedcnt = 0
for i in range(start, loopval+1):
  clearConsole()
  print(f"{len(resultlist)}개의 단어가 수집되었습니다.")
  print(str(i)+'/'+str(loopval))
  print(round(time.time())-starttime)
  try:
    F()
  except:
    driver.quit()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.image': 2})
    driver = webdriver.Chrome("C:/Users/superhoy/Desktop/basiccrawling/chromedriver.exe", chrome_options=options)
    driver.set_page_load_timeout(10)
    i-=1

  if i%10000==0:
    resultlist=list(dict.fromkeys(resultlist))
    with open(str(math.floor((i/10000)-1))+'0001-'+str(math.floor(i/10000))+'0000.txt', 'w', encoding='utf8') as f:
      for item in resultlist:
        f.write("%s\n" % item)
    resultlist.clear()


with open(str(math.floor(i/10000))+'0001-'+str(i)+'.txt', 'w', encoding='utf8') as f:
  for item in resultlist:
    f.write("%s\n" % item)

driver.quit()
