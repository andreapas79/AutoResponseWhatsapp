from selenium import webdriver
import datetime
import random

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = 'ContactName' #insert name of your contact
msg = 'message1', 'message2', 'message3', 'message4', 'message5'

input('Enter anything after scanning QR code')
i = 0
b = True
nuovomsq = False
nmsg = 0
while (i < 10):
    count = driver.find_elements_by_class_name("message-in")
    if (nmsg != len(count)):
        nmsg = len(count)
        nuovomsq = True
    if (int(datetime.datetime.now().strftime("%M")) % 2 == 0 and b):
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('_13mgZ')
        msg_box.send_keys("io sono qui a non fare nulla")
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        i += 1
        b = False
    if (int(datetime.datetime.now().strftime("%M")) % 2 == 1):
        b = True
    if (nuovomsq):
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_13mgZ')
        msg_box.send_keys(msg[random.randrange(0, 7)])
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        nuovomsq = False
