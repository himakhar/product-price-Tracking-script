# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:43:41 2019

@author: himakhar
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/ADISA-BP004-Weight-Casual-Backpack/dp/B07G3CG9FC/ref=sr_1_5?crid=3KMXWHV9HW65V&keywords=bag+for+men&qid=1562438793&s=gateway&sprefix=bag%2Caps%2C287&sr=8-5'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content,'html.parser')
    
    title= soup.find(id='productTitle').get_text()
    
    price= soup.find(id='priceblock_ourprice').get_text()
    
    converted_price= float(price[1:5])
    
    if(converted_price < 5.99):
        send_mail()
        
    print(converted_price)    
    print(title.strip())
    
    if(converted_price > 5.99):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('himakhar007@gmail.com','human1234')
    
    subject ='price fell down!'
    body = 'check the amazon link https://www.amazon.in/ADISA-BP004-Weight-Casual-Backpack/dp/B07G3CG9FC/ref=sr_1_5?crid=3KMXWHV9HW65V&keywords=bag+for+men&qid=1562438793&s=gateway&sprefix=bag%2Caps%2C287&sr=8-5'
    
    msg=f'Subject: {subject}\n\n{body}'
    
    server.sendmail('himakhar007@gmail.com','dhargiri867@gmail.com',msg)
    
    print('hey Email has  been sent!')
    

    
    server.quit()

check_price()

'''while(True):
    check_price()
    time.sleep(60*60)'''
    
    
