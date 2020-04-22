from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class Whois(object):

	def __init__(self, url):
		self.url = url

	def lookup(self):
		driver = webdriver.Chrome("C:/Users/Tyler/PycharmProjects/WebScanner/Driver/chromedriver.exe")
		driver.get("https://www.whois.net/")
		search = driver.find_element_by_id("domain_search")
		search.send_keys(self.url)
		search.send_keys(Keys.ENTER)
		driver.implicitly_wait(100)
		search = driver.find_element_by_id("whois_result_data").text
		return search
