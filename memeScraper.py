import requests
from time import sleep
from datetime import datetime
from selenium.webdriver import Edge
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Edge Browser

caps = DesiredCapabilities().EDGE
caps["pageLoadStrategy"] = "eager"  
driver = Edge(executable_path=r'C:\\Program Files (x86)\\Python38-32\\EdgeDriver\\msedgedriver.exe', capabilities=caps)
driver.implicitly_wait(10)
driver.maximize_window()

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
    old = 0
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

            # If the post is not from today, keep count
            else:
                old += 1

        except:
            continue

driver.quit()