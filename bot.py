import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from countdown import countdown
import pyautogui
import pynput
import threading
from pynput.mouse import Button,Controller

class waktu():
   def waktumundur():

        menit = 0
        detik = 3
        
        countdown(menit,detik)
class Autocheck():
    def autocheck(self):
        waktu.waktumundur()
        print("Bot sedang berjalan...\n")
        browser = webdriver.Chrome('webdriver/chromedriver.exe')

        url = "https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2Fproduct%2F52635036%2F6138232981%2F"
        browser.get(url)
        bukafileakun = open("akun.txt")
        bacaakun = bukafileakun.readlines()
        username = bacaakun[0]
        password = bacaakun[1]
        AkunID = browser.find_element_by_class_name('_56AraZ')
        AkunID.send_keys(username)
        AkunID.send_keys(Keys.TAB,password)
        AkunID.send_keys(Keys.ENTER)
        # bukalist = open("linkcom.txt")
        # bacafile = bukalist.readlines()
        targeturl = "https://shopee.co.id/Samsung-A01-Core-2-32GB-Black-i.52635036.6138232981"
        browser.get(targeturl)
        # checkoutid = browser.find_element_by_class_name("btn btn-solid-primary btn--l YtgjXY")
        # checkoutid.click()
        
        checkoutid = browser.find_element_by_class_name('btn btn-solid-primary btn--l YtgjXY')
        checkoutid.send_keys('btn btn-solid-primary btn--l YtgjX')
        print("Berhasil Checkout")

namaaplikasi = "Bot Pro 1.0 Develop By Rizqi Wijaya"
print(namaaplikasi)
auto = Autocheck()
auto.autocheck()

