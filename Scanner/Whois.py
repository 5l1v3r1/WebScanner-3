from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup as bs
import requests


class Whois(object):

	def __init__(self, url):
		self.url = url

	def lookup(self):
		# driver = webdriver.Chrome("C:/Users/Tyler/PycharmProjects/WebScanner/Driver/chromedriver.exe")
		# driver.get("https://www.whois.net/")
		# search = driver.find_element_by_id("domain_search")
		# driver.implicitly_wait(5)
		# search.send_keys(self.url)
		# search.send_keys(Keys.ENTER)
		# driver.implicitly_wait(5)
		# search = driver.find_element_by_id("whois_result_data").text
		# return search
		url = "http://who.is/whois/" + self.url[8: len(self.url)]
		page = requests.get(url)
		soup = bs(page.text, 'html.parser')
		results = soup.find_all(class_='col-md-12 queryResponseBodyValue')
		string = ""
		for result in results:
			string += result.prettify()
		return string
