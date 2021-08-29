import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def main(Search):
    # if sys.platform=="linux":
    #     driver=os.path.join(os.getcwd(),'chromedriver')
    # elif sys.platform.startswith("win"):
    #     driver=os.path.join(os.getcwd(),'chromedriver.exe')
    driver=webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(2)
    driver.find_element(By.NAME,"q").send_keys(Search)
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
    time.sleep(10)
if __name__=="__main__":
    Search=input("Search: ")
    main(Search)