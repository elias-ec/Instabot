from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randrange
import time

##
##

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')

time.sleep(2)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]"))
    ) #wir warten 10 sekunden ob der webdriver die ID findet
    element.click()

    search = driver.find_element_by_name("username")
    search.send_keys("YourUsername")#############
    time.sleep(randrange(1, 6))#wir warten zufällige sekunden 1-6

    search = driver.find_element_by_name("password")
    search.send_keys("YourPassword")#############
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))
        )  # wir warten 10 sekunden ob der webdriver die ID findet
        element.click()  # Notifications werden abgelehnt
        time.sleep(3)
    finally:
        search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys("YourUser/Hashtag")  ###########
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        time.sleep(1)
        search.send_keys(Keys.RETURN)
        time.sleep(randrange(3, 8))# im suchfeld wird gesucht und durch zweimalige bestätigung durch return das Ergebniss ausgewählt

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div"))
        )  # wir warten 10 sekunden ob der webdriver die ID findet
        element.click()  # erster beitrag wird ausgewählt
        time.sleep(6)

        i = 0
        while i < 10:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "fr66n"))
            )  # wir warten 10 sekunden ob der webdriver die ID findet
            element.click()  # Beirag geliked
            time.sleep(randrange(3, 15))

            search = driver.find_element_by_tag_name("body")
            search.send_keys(Keys.ARROW_RIGHT)  # nächster beitrag
            time.sleep(randrange(1, 7))
            i = i + 1



finally:
    print("Finished")
    time.sleep(500)
    driver.quit()


