###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# An inmate model. We expect to come in knowing name and birth year, and populate other data from the inmate registry.
###

class Inmate:
	def __init__ (self, firstName = '', lastName = '', middleName = '', birthYear = ""):
		self.firstName = firstName
		self.lastName = lastName
		self.middleName = middleName
		self.birthYear = birthYear
		self.docID = ''
		self.race = ''
		self.gender = ''
		self.birthDay = ''
		self.daneID = ''

	def setFirstName (self, firstName):
		self.firstName = firstName

	def setLastName (self, lastName):
		self.lastName = lastName

	def setMiddleName (self, middleName):
		self.middleName = middleName

	def setbirthYear (self, birthYear):
		self.birthYear = birthYear

#do not update if do not have good data
	def setDocID (self, docID):
		if docID and docID != "COULD NOT RETRIEVE": self.docID = docID

	def setRace (self, race):
		if race and race != "COULD NOT RETRIEVE": self.race = race

	def setGender (self, gender):
		if gender and gender != "COULD NOT RETRIEVE": self.gender = gender

	def setBirthYear (self, birthYear):
		if birthYear and birthYear != "COULD NOT RETRIEVE": self.birthYear = birthYear

	def setDaneID (self, daneID):
		if daneID != "COULD NOT RETRIEVE": self.daneID = daneID

	def __str__ (self):
		return ','.join([self.daneID, self.firstName, self.lastName, self.middleName, str(self.birthYear), str(self.docID), self.race, self.gender])