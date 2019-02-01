import time,re
import sys
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from slenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import browser_unit
import random
#import google_search

MALE_EMAIL = 'adfisher0001@gmail.com'
PASSWORD = '1234@5678'

FEMALE_EMAIL = 'adfisher0002@gmail.com'

SEPARATOR = '@|'



from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
  def __init__(self):
    self.reset()
    self.fed = []
  def handle_data(self, d):
    self.fed.append(d)
  def get_data(self):
    return ''.join(self.fed)

def strip_tags(html):
  s = MLStripper()
  s.feed(html)
  return s.get_data()  
 

class GoogleAdsSettingsUnit(browser_unit.BrowserUnit):
	
	def __init__(self, browser, log_file, unit_id, treatment_id, headless=False, proxy=None):
        browser_unit.BrowserUnit.__init__(self, browser, log_file, unit_id, treatment_id, headless, proxy=proxy)


    def create_user(self,gender):
        if (gender=='male'):
            user_email = MALE_EMAIL
         else:
            user_email = FEMALE_EMAIL
        user_password = PASSWORD

    #login part

    self.driver.get("https://accounts.google.com")
    login_email =self.find_elements_by_css_selector("#identifierId")
    login_next = self.find_elements_by_css_selector(".DL0QTb content.CwaK9 > span.RveJvd.snByac")

    login_next.click()

    login_password = self.find_elements_by_css_selector("div.aXBtI.I0VJ4d.Wic03c div.Xb9hP > input.whsOnd.zHQkBf")
    login_next2 =self.find_elements_by_css_selector(".DL0QTb > content.CwaK9")

    login_next2.click()




	def collect_gender(self,reloads,delay.site,file_name=None):
		if file_name == None:
            file_name = self.log_file
        rel = 0
        while (rel < reloads):  # number of reloads on sites to capture all ads
            time.sleep(delay)
            s = datetime.now()
            ## write code here
            self.save_gender(file_name)
            e=datetime.now()
            self.log('measurement', 'loadtime', str(e-s))

                ################################ code for signout #######################################
            rel = rel + 1

    def save_gender(self, file):
    	driver = self.driver
        id = self.unit_id
        sys.stdout.write(".")
        sys.stdout.flush()
        driver.set_page_load_timeout(60)
        driver.get("https://myaccount.google.com/")
        tim = str(datetime.now())
        data_per = driver.find_elements_by_css_selector("a.VZLjze.Wvetm.zCVEd.EhlvJf:nth-child(3) > div.GiKO7c")
        data_per.click()
        to_ad_set =driver.find_elements_by_css_selector("article.GIxHAe.gd0DBb:nth-child(6) div.XLK0Od.Aovece div.ahh38c div.ugt2L.ul8zCc.aK2X8b.t97Ap:nth-child(3) div.VfPpkd-ksKsZd-XxIAqe a.VZLjze.Wvetm.N5YmOc.kJXJmd > div.mtfBU")
        to_ad_set.click()
        gender = driver.find_elements_by_css_selector("div.fRYEGc:nth-child(2) > div.c7O9k").get_attribute('innerHTML').strip()
 		demographic = strip_tags("@|"+gender).encode("utf8")
        ##self.log('measurement', 'gender', demographic)
        if(gender != "Female" && gender != "Male"):
        	self.log('measurement', 'gender', 'no inference')
        else:
        	self.log('measurement', 'gender', demographic)





