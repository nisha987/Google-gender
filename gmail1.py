import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()


browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('16ucc063@lnmiit.ac.in')
nextButton = browser.find_element_by_xpath(".//*[@id='identifierNext']/content/span")
nextButton.click()

time.sleep(10)

passwordElem = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/content[1]/section[1]/div[1]/content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')

passwordElem.send_keys('7737028644')

signinButton = browser.find_element_by_css_selector('#passwordNext')
signinButton.click()

time.sleep(10)

#visit all websites

url_list =["https://realpython.com/modern-web-automation-with-python-and-selenium/", "https://www.youtube.com/watch?v=XqvCNYEqy34"]

for url in url_list:
	browser.get(url)
	time.sleep(10)



browser.get("https://adssettings.google.com/authenticated")

gender =browser.find_element_by_css_selector('div.KqP3nc div.ym7eO.vmi1sd div.fRYEGc:nth-child(2) > div.c7O9k').text
print(gender)

#data_per = browser.find_elements_by_css_selector("a.VZLjze.Wvetm.zCVEd.EhlvJf:nth-child(3) > div.GiKO7c")
#data_per.click()


#to_ad_set =browser.find_elements_by_css_selector("article.GIxHAe.gd0DBb:nth-child(6) div.XLK0Od.Aovece div.ahh38c div.ugt2L.ul8zCc.aK2X8b.t97Ap:nth-child(3) div.VfPpkd-ksKsZd-XxIAqe a.VZLjze.Wvetm.N5YmOc.kJXJmd > div.mtfBU")
#to_ad_set.click()


##gender = browser.find_elements_by_css_selector("div.fRYEGc:nth-child(2) > div.c7O9k").get_attribute('innerHTML').strip()


