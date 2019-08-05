###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# Inmate getter: takes a list of inmates and pulls additional data from Wisconsin's Offender Locator at https://appsdoc.wi.gov/lop/home.do.
###
from __future__ import print_function
import os, os.path

from inmate_collection import *
from inmate_getter_config_constants import *
from jailpop_args_parse import *



class InmateGetter:
	def __init__ (self, inmateRegistryScraper):
		self.inmateRegistryScraper = inmateRegistryScraper

	###
	#	Reads in a list of inmates from a CSV. These inmates are the ones we will gather additional information about.
	#	Input: void.
	#	Output: a populated InmateCollection
	##
	def loadInmates (self):
		global args
		inmates = InmateCollection()

		inmateFile = open(args.infile, FILE_MODE_READ)

		isFirstLine = True
		for line in inmateFile:
			print("line", line)
			if isFirstLine:
				isFirstLine = False
				if IGNORE_HEADER_ROW:
					continue
			inmates.addFromCSV(line)


		inmateFile.close()

		return inmates

	###
	#	Uses our interface to the inmate data source to get additional inmate data.
	#	Input: a populated InmateCollection
	#	Output: a populated InmateCollection with additional details on each inmate
	##
	def enhanceInmateData (self, inmates):
		for inmate in inmates:
			self.inmateRegistryScraper.addEnhancedInmateData(inmate)

		return inmates

	###
	#	Writes out our enhanced inmate data to a CSV.
	#	Input: a populated InmateCollection
	#	Output: void -- except for file system
	##
	def saveInmateData (self, inmates):
		global args
		outputFile = open(args.outfile, FILE_MODE_WRITE)

		for inmate in inmates:
			outputFile.write(str(inmate) + "\n")

		outputFile.close()

	###
	#	Writes out our enhanced inmate data to a CSV.
	#	Input: a populated InmateCollection
	#	Output: void -- except for file system
	##
	def run (self):
		global args
		args = parse_arguments_fix()
		inmates = self.loadInmates()
		inmates = self.enhanceInmateData(inmates)
		self.saveInmateData(inmates)
