###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# A group of inmates for use in the inmate getter. Handles population of inmates from CSV data.
###

from inmate import *
from inmate_data_mapper import *

class InmateCollection:

	def __init__ (self):
		self.inmates = []

	def __iter__ (self):
		return iter(self.inmates)

	def add (self, inmate):
		self.inmates.append(inmate)

	def addFromCSV (self, line):
		#unpack our CSV line
		inmateData = ','.split(line)

		inmateDictionary = InmateDataMapper.map(line)

		inmate = Inmate(inmateDictionary['firstName'], inmateDictionary['lastName'], inmateDictionary['middleName'], inmateDictionary['birthYear'])
		self.add(inmate)


