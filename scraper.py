from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

page = requests.get("https://www.twitch.tv/moistcr1tikal")
soup = BeautifulSoup(page.content, 'html.parser')

driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/videos/742841137?filter=archives&sort=time")



file = open('comments.txt', 'a', encoding='utf8')
while True:
    command = input("Scrape stop or pass: ")
    if command == "scrape":
        elem = ""

        #elem = driver.find_element_by_class_name("text-fragment")
        for comment in driver.find_elements_by_class_name("text-fragment"):
            print(comment.text)
            file.write(comment.text + "\n")
        #for comment in driver.find_element_by_tag_name("img"):
        #    print(comment.text)

    elif command == "pass":
        continue
    else:
        file.close()
        break

