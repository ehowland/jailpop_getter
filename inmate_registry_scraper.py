###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# Pulls additional data from Wisconsin's Offender Locator at https://appsdoc.wi.gov/lop/home.do.
#
# To get the requests module: python.exe -m pip install requests
###

import re
import requests
import time

from inmate_registry_scraper_config_constants import *

class InmateRegistryScraper:

	def __init__ (self):
		# Precompiling our regex to avoid load
		self.docPattern = re.compile(DOC_NUMBER_REGEX_PATTERN)
		self.racePattern = re.compile(RACE_REGEX_PATTERN)
		self.sexPattern = re.compile(SEX_REGEX_PATTERN)
		self.session = None

	def addEnhancedInmateData (self, inmate):
		html = self.pullInmateHTML(inmate)

		docNumber = self.getDocNumberFromHTML(html)
		race = self.getRaceFromHTML(html)
		sex = self.getSexFromHTML(html)
		
		#birthDay = self.getBirthDayFromHTML(html)

		inmate.setDocNumber(docNumber)
		inmate.setRace(race)
		inmate.setSex(sex)
		#inmate.setBirthDay = birthDay

		return inmate

	def startSession (self):
		session = requests.Session()

		# initialize cookies
		response = session.get(INMATE_REGISTRY_URL)

		#self.dumpHTML(response.text, 'welcome_page_html_dump.html')

		# set the "accept privacy policy" cookie
		acceptance_cookie = requests.cookies.create_cookie(domain=INMATE_REGISTRY_DOMAIN, name='Accept', value='true')
		session.cookies.set_cookie(acceptance_cookie)

		self.session = session

	def checkSession (self):
		if self.session == None: # Currently not handling session timeouts.
			self.startSession()

	def pullInmateHTML (self, inmate):
		# Make sure our session is alive and exists
		self.checkSession()

		post_data = self.getSearchPostData(inmate)

		response = self.session.post(INMATE_REGISTRY_SEARCH_URL, data=post_data)
		html = response.text

		#self.dumpHTML(html, 'specific_inmate_html_dump.html')

		time.sleep(TIMEOUT_BETWEEN_REQUESTS) # let's not DDOS the server by accident

		return html

	def getSearchPostData (self, inmate):
		post_data = {
			'view': 'demographics',
			'searchpage': 'basic',
			'pageSize': 25,
			'sortBy': 2,
			'helpMenu': '/lop/help/PLHelp.htm#Search+Tips',
			'LAST_NAM': inmate.lastName.strip(),
			'FIRST_NAM': inmate.firstName.strip(),
			'MID_NAM': inmate.middleName.strip(),
			'RACE': '',
			'GENDER': inmate.sex.strip(),
			'BIRTH_YEAR': '', #inmate.birthYear,
			'ADR_CITY': '',
			'ADR_COUNTY': '',
			'ADR_MIN_ZIP': '',
			'ADR_MAX_ZIP': '',
			'DOC_NUM': ''
		}

		return post_data

	def getDocNumberFromHTML (self, html):
		matches = re.findall(self.docPattern, html)
		print("Start===============================")
		print(html)
		print("End===============================")
		print("matches", matches)
		if not matches or len(matches) == 0:
			return 'COULD NOT RETRIEVE'

		return matches[0]

	def getRaceFromHTML (self, html):
		matches = re.findall(self.racePattern, html)

		if not matches or len(matches) == 0:
			return 'COULD NOT RETRIEVE'

		return matches[0]

	def getSexFromHTML (self, html):
		matches = re.findall(self.sexPattern, html)

		if not matches or len(matches) == 0:
			return 'COULD NOT RETRIEVE'

		return matches[0]

	def getBirthDayFromHTML (self, html):
		a = 1

	def dumpHTML (self, html, filename):
		#testing method

		f = open(filename, 'w')

		f.write(html)

		f.close()
