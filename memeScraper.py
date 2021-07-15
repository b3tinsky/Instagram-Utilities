import requests
import re
import backopyConfig
from time import sleep
from datetime import datetime, date
from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from getpass import getpass
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import csv
# from selenium.webdriver.edge.options import Options
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# Edge Browser

caps = DesiredCapabilities().EDGE
caps["pageLoadStrategy"] = "eager"  
driver = Edge(executable_path=r'C:\\Program Files (x86)\\Python38-32\\EdgeDriver\\msedgedriver.exe', capabilities=caps)
driver.implicitly_wait(10)
driver.maximize_window()


# TWITTER MEMES

twitterAccounts = [
    'https://twitter.com/_thememefactory',
    'https://twitter.com/DankMemesBot420',
    'https://twitter.com/314I59',
    'https://twitter.com/MemeLegend_',
    'https://twitter.com/DankRedditBot',
    'https://twitter.com/r_memes_',
    'https://twitter.com/memeadikt',
    'https://twitter.com/MemesCentraI',
    'https://twitter.com/_auntysocial',
    ]

now = str(datetime.now())

for twitterAccount in twitterAccounts:
    driver.get(twitterAccount)
    # TODO: Scroll the page several times
    sleep(20)

    cards = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div')
    for i in range(0,len(cards)):

        try:
            dateCard = cards[i].find_element_by_xpath('./div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time')
            date = dateCard.get_attribute('datetime')

            if(date[0:10] == now[0:10]):
                imgCard = cards[i].find_element_by_xpath('./div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img')
                imgUrl = imgCard.get_attribute('src')
                
                img_data = requests.get(imgUrl).content
                name = 'C:\\Users\\B3TINSKY\\Pictures\\Backopy Memes\\Waiting room\\' + imgUrl.split('/')[-1].split('?')[0] + '.jpg'

                with open(name, 'wb') as handler:
                    handler.write(img_data)

            else:
                continue

        except:
            continue






# INSTAGRAM MEMES

instagramAccounts = [
    'https://www.instagram.com/95points/',
    'https://www.instagram.com/cumfather.exe/',
    'https://www.instagram.com/bot.inspector/',
    'https://www.instagram.com/topmemeposter/',
    'https://www.instagram.com/mr.memeasauraus/',
    'https://www.instagram.com/humourbanks/',
    'https://www.instagram.com/cringe.department/',
    'https://www.instagram.com/jellymeme_/',
    'https://www.instagram.com/dankgary/',
    'https://www.instagram.com/muffin_time_memes/',
    'https://www.instagram.com/shitheadsteve/',
    'https://www.instagram.com/epicallyepicmemes/'
    ]

# Textual month, day and year	
today = date.today()
todayFormatted = today.strftime("%B %d, %Y")

# Extracts filename that comes after dimension. Example: .../s640x640/name.jpg/...
namePattern = re.compile(r"""
    (.*?)                   
    (s?p?\d{3,}x\d{3,}/)
    (.*?\.jpg)                   
    (.*?)                   
    """, re.VERBOSE)

datePattern = re.compile(r"""
    (.*?\son\s)                   
    (.*?)
    (\..*?)                                     
    """, re.VERBOSE)

# LOGIN
driver.get('https://www.instagram.com/')
sleep(60)
inputField = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
inputField.send_keys(backopyConfig.USERNAME)
passwordField = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordField.send_keys(backopyConfig.PASSWORD)
passwordField.send_keys(Keys.RETURN)
sleep(30)

for instagramAccount in instagramAccounts:
    driver.get(instagramAccount)
    sleep(10)
    
    cards = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[*]/article/div[1]/div/div/div')

    for i in range(len(cards)):
        try:
            card = cards[i].find_element_by_xpath('./a')
            cardExtraInfo = card.find_element_by_xpath('./div[1]/div[1]/img')
            # Only matches photos, not videos or reels
            if(cardExtraInfo.get_attribute('alt')[0:8] == 'Photo by'):
                imgDate = datePattern.search(cardExtraInfo.get_attribute('alt'))

                # Only matches today's uploads
                if (todayFormatted == imgDate.group(2)):
                    card.click()
                    sleep(5)
                    bigMeme = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/img')
                    imgUrl = bigMeme.get_attribute('src')
                    imgData = requests.get(imgUrl).content
                    imageName = namePattern.search(imgUrl)
                    name = 'C:\\Users\\B3TINSKY\\Pictures\\Backopy Memes\\Waiting room\\' + imageName.group(3)



                    with open(name, 'wb') as handler:
                        handler.write(imgData)
                    sleep(5)
                    card.send_keys(Keys.ESCAPE)

            else:
                continue
        except:
            continue





driver.quit()