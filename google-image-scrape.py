"""
Francesco Gerratana 2022, www.nextechnics.com
Simple example web scrape with python 3 and Selenium 4.1.3 + ChromeDriver 99.0.4844.51,
Run before pip install to install the necessary packages
"""
import time
import os
import urllib
import urllib.request
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:

    driver.get('https://images.google.com/');

    time.sleep(5)
    
    bt = driver.find_element(by=By.ID, value='L2AGLb')

    bt.click()
    
    time.sleep(0.2)
 
    search_box = driver.find_element(by=By.NAME, value='q')

    search_box.send_keys('Chihuahua')

    search_box.submit()

    time.sleep(0.2)

    counter = 0
    salvate = 0
    
    dest = os.path.join(os.getcwd(),"img")
    if not os.path.exists(dest):
        os.makedirs(dest)
   
    for _ in range(2):
        driver.execute_script("window.scrollBy(0,10000)")
         
    for x in driver.find_elements(by=By.XPATH, value='//img[contains(@class,"rg_i Q4LuWd")]'):
       
        counter = counter + 1
        
        
        if not x.get_attribute('src') == "": 
        
            img = x.get_attribute('src')    
            
            new_filename = dest+"\img_"+str(counter)+".jpg"
            
            #print(new_filename)
            try:
                urllib.request.urlretrieve(img, new_filename)
                salvate += 1
            except Exception as e:
                print(e)
                
                
    print('trovate:'+str(counter)+' salvate:'+str(salvate))
    time.sleep(0.2) 

    driver.quit()