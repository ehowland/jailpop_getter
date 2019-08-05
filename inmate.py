###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# An inmate model. We expect to come in knowing name and birth year, and populate other data from the inmate registry.
###

class Inmate:
	def __init__ (self, firstName = '', lastName = '', middleName = '', birthYear = 1):
		self.firstName = firstName
		self.lastName = lastName
		self.middleName = middleName
		self.birthYear = birthYear
		self.docNumber = ''
		self.race = ''
		self.sex = ''
		self.birthDay = ''

	def setDocNumber (self, docNumber):
		self.docNumber = docNumber

	def setRace (self, race):
		self.race = race

	def setSex (self, sex):
		self.sex = sex

	def setBirthDay (self, birthDay):
		self.birthDay = birthDay

	def __str__ (self):
		return ','.join([self.firstName, self.lastName, self.middleName, str(self.birthYear), str(self.docNumber), self.race, self.sex])