import time, re                                                     # time.sleep, re.split
import sys                                                          # some prints
from selenium import webdriver                                      # for running the driver on websites
from datetime import datetime                                       # for tagging log with datetime
from selenium.webdriver.common.keys import Keys                     # to press keys on a webpage
from selenium.common.exceptions import NoSuchElementException
import random


# get login ids
def clean(s):
    toks = s.strip().split(' ')
    return toks

with open('FEMALE.txt') as f:
    FEMALE_CREDENTIALS = map(clean, f.readlines())
    print FEMALE_CREDENTIALS

with open('MALE.txt') as f:
    MALE_CREDENTIALS = map(clean, f.readlines())


with open('yoga.txt') as f:
	URL_LIST = f.readlines()
	print URL_LIST

def get_random_entry(array):
	index = random.randrange(1,len(array)-1)
	return array[index]

def get_login_credentials(gender):
    '''returns (username, password)'''
    if (gender=='male'): #male
      return get_random_entry(MALE_CREDENTIALS)
    else: # female 
      return get_random_entry(FEMALE_CREDENTIALS)


#def get_site_file():
#    return get_random_entry(URL_LIST)
    

def find_gender(f_gender):
	browser = webdriver.Firefox()
	
	[user_email, user_password] = get_login_credentials(f_gender)


	browser.get('http://gmail.com')

	emailElem = browser.find_element_by_id('identifierId')
	emailElem.send_keys(user_email)
	nextButton = browser.find_element_by_xpath(".//*[@id='identifierNext']/content/span")
	nextButton.click()

	time.sleep(10)

	passwordElem = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/content[1]/section[1]/div[1]/content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')

	passwordElem.send_keys(user_password)

	signinButton = browser.find_element_by_css_selector('#passwordNext')
	signinButton.click()

	time.sleep(10)

	#visit all websites

	#url_list =["https://realpython.com/modern-web-automation-with-python-and-selenium/", "https://www.youtube.com/watch?v=XqvCNYEqy34"]

	for url in URL_LIST:
		print(url)
		browser.get(url)
		time.sleep(10)

	

	browser.get("https://adssettings.google.com/authenticated")

	gender =browser.find_element_by_xpath('/html[1]/body[1]/div[4]/c-wiz[1]/c-wiz[1]/div[1]/c-wiz[3]/div[1]/div[1]/ul[1]/li[2]/div[2]').text
	print(gender)

	#data_per = browser.find_elements_by_css_selector("a.VZLjze.Wvetm.zCVEd.EhlvJf:nth-child(3) > div.GiKO7c")
	#data_per.click()


	#to_ad_set =browser.find_elements_by_css_selector("article.GIxHAe.gd0DBb:nth-child(6) div.XLK0Od.Aovece div.ahh38c div.ugt2L.ul8zCc.aK2X8b.t97Ap:nth-child(3) div.VfPpkd-ksKsZd-XxIAqe a.VZLjze.Wvetm.N5YmOc.kJXJmd > div.mtfBU")
	#to_ad_set.click()


	##gender = browser.find_elements_by_css_selector("div.fRYEGc:nth-child(2) > div.c7O9k").get_attribute('innerHTML').strip()
find_gender('male')
	