"""
@author: Elias Eckermann
"""
from tkinter import *  # --> Import everything from tkinter für gui
##Bot:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randrange
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

##########################################################################################################
# start Bot ! ! !
def startBot():
    driver.get('https://www.instagram.com/')

    time.sleep(2)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]"))
        )  # waiting 10 sec until element was found
        element.click()

        search = driver.find_element_by_name("username")
        search.send_keys(eun.get())  # U S E R N A M E
        time.sleep(randrange(1, 6))  # waiting random time (1-6sec)

        search = driver.find_element_by_name("password")
        search.send_keys(epw.get())  # P A S S W O R D
        search.send_keys(Keys.RETURN)
        time.sleep(5)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "cmbtv"))
            )
            element.click()
            time.sleep(3)
        finally:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))
                )
                element.click()  # reject Notifications
                time.sleep(3)
            finally:
                search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
                search.send_keys(ehu.get())  # H A S H T A G   O R   U S E R
                time.sleep(1)
                search.send_keys(Keys.RETURN)
                time.sleep(3)
                search.send_keys(Keys.RETURN)
                time.sleep(randrange(2,
                                     5))  # Bot searches for account or user
                if followVar == True:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//button[text()="Follow"]'))
                    )
                    element.click()
                time.sleep(randrange(1, 5))

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "eLAPa"))
                )
                element.click()  # select first picture
                time.sleep(6)


                i = 0
                while i < int(eam.get()):  # A M O U N T   O F   L I K E S
                    try:
                        element = driver.find_element_by_class_name("fr66n")
                        element.click()
                        time.sleep(randrange(1, 5)) # picture liked

                        search = driver.find_element_by_tag_name("body")
                        search.send_keys(Keys.ARROW_RIGHT)  # next picture
                        time.sleep(randrange(2, 13))

                        if i % 100 == 0:  # If Likes can be divided by 100...
                            print("sleeping...")
                            time.sleep(randrange(15, 40))  # ... Bot waits longer


                    except:
                        try:
                            element = driver.find_element_by_class_name("aOOlW   HoLwm ")
                            element.click()  # Bot confirms "Try Again"
                            time.sleep(randrange(1, 7))

                            element = driver.find_element_by_class_name("fr66n")
                            element.click() # picture liked
                            time.sleep(randrange(1, 5))

                            search = driver.find_element_by_tag_name("body")
                            search.send_keys(Keys.ARROW_RIGHT)  # next picture
                            time.sleep(randrange(2, 13))

                            if i % 100 == 0:  # If likes can be divided by 100...
                                print("sleeping...")
                                time.sleep(randrange(15, 40))  # ...Bot waits longer
                        except:
                            search = driver.find_element_by_tag_name("body")
                            search.send_keys(Keys.ARROW_RIGHT)  # next picture
                            time.sleep(randrange(2, 13))
                            print("Ein Element nicht gefunden!!!")

                    i = i + 1
                    print(i)





    finally:
        print("Finished!!!")
        time.sleep(10)
        driver.quit()
        quit()


##########################################################################################################
# ende Bot  ! ! !


# GUI:
followVar = False

root = Tk()

lw = Label(root, text="Welcome to the simple Instabot Project by elias-e")
lw.grid(row=0, column=0 & 1)

lun = Label(root, text="Your Username")
lun.grid(row=1, column=0)

username_text = StringVar()
eun = Entry(root, textvariable=username_text)
eun.grid(row=1, column=1)

lpw = Label(root, text="Your Password")
lpw.grid(row=2, column=0)

password_text = StringVar()
epw = Entry(root, textvariable=password_text)
epw.grid(row=2, column=1)

lhu = Label(root, text="Hashtag or User")
lhu.grid(row=3, column=0)

hashtagoruser_text = StringVar()
ehu = Entry(root, textvariable=hashtagoruser_text)
ehu.grid(row=3, column=1)

lam = Label(root, text="Amount of Likes")
lam.grid(row=4, column=0)

amount_text = StringVar()
eam = Entry(root, textvariable=amount_text)
eam.grid(row=4, column=1)

l4 = Label(root, text="Follow?")
l4.grid(row=5, column=0)


def follow():
    global followVar
    if followVar == False:
        followVar = True
        followbt.configure(bg="green")
    else:
        followVar = False
        followbt.configure(bg='gray')


followbt = Button(root, text="Yes", width=12, command=follow, bg='gray')
followbt.grid(row=5, column=1)


def startClick():
    print("Ok bestätigt")
    if len(eun.get()) == 0 or len(epw.get()) == 0 or len(ehu.get()) == 0 or len(eam.get()) == 0:
        errorwindow = Tk()
        l5 = Label(errorwindow, text="Please fill in all fields", fg="red")
        l5.grid(row=1, column=1)

        def okClick():
            errorwindow.destroy()

        okbt = Button(errorwindow, text="Ok", width=12, command=okClick)
        okbt.grid(row=2, column=1)
        errorwindow.mainloop()
    else:
        print("go")
        gowindow = Tk()
        l6 = Label(gowindow,
                   text="Bot starts. You are responsible for the use of this software. Please confirm with Ok.",
                   fg="red")
        l6.grid(row=1, column=1)

        gobt = Button(gowindow, text="Ok", width=12, command=startBot)
        gobt.grid(row=2, column=1)
        print("starting...")


def cancelClick():
    quit()


startbt = Button(root, text="Ok", width=12, command=startClick)
startbt.grid(row=6, column=0)

cancelbt = Button(root, text="Cancel", width=12, command=cancelClick)
cancelbt.grid(row=6, column=1)

root.mainloop()  # ende des windows
