###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# Inmate getter: takes a list of inmates and pulls additional data from Wisconsin's Offender Locator at https://appsdoc.wi.gov/lop/home.do.
###
from __future__ import print_function
import os, os.path, csv

from inmate_collection import *
from inmate import *
from inmate_getter_config_constants import *
from jailpop_args_parse import *



class InmateGetter:
	def __init__ (self, inmateRegistryScraper):
		self.inmateRegistryScraper = inmateRegistryScraper


	def load_csv_one_dict_each_line(self):
		
		with open(args.infile) as csvfile:
			reader = csv.DictReader(csvfile)
			if args.verbose >= 7: print("Field names: ", reader.fieldnames)
			inmate_list = []
			incount = 0
			for rec in reader:
				if args.verbose >= 3: print(".")
				if args.verbose >= 7: print(rec)
			
				#if (incount % 100) == 0: print("\n      read in line:",incount)
				incount += 1
				inmate_list.append(rec)
				
			
			if args.verbose >= 3:print("\nRead in people to scrape got:",incount)
			return inmate_list
	###
	#	Reads in a CVS file with inmates to be checked
	#	Input: void.
	#	Output: a populated InmateCollection
	##
	def loadInmates (self):
		global args
		inmates = InmateCollection()
		inmate_dict_list = self.load_csv_one_dict_each_line()

		for inmate_dict in inmate_dict_list:
			this_inmate = Inmate()
			#new person don't want carryover last person
			lastname = firstname = firstmiddlename = middlename = first_middle = middle_init = ''  
			
			if args.verbose >= 3: print(inmate_dict, len(inmate_dict_list))
			#since the name comes in from the database as one field have to split it and then load up data
			name = inmate_dict.get('Name')
			name_list = name.split(",")
			
			if len(name_list) >= 1: #at least one name
				lastname = name_list[0]
			if len(name_list) > 1: 
				firstmiddlename = name_list[1].strip()
			
			if firstmiddlename:
				firstmiddle_list = firstmiddlename.split(" ", 1)
				if len(firstmiddle_list) >= 1:
					firstname = firstmiddle_list[0]
				if len(firstmiddle_list) > 1:
					middlename = firstmiddle_list[1]
				
			
			
			
			if middlename: middle_init = middlename[0] # take first letter
			
			if args.verbose >= 3: print("split names",name,name_list,"|"+firstname+"|"+firstmiddlename+"|"+middlename+"|"+first_middle+"|"+middle_init)
			
			this_inmate.setFirstName(firstname.strip())
			this_inmate.setLastName(lastname.strip())
			this_inmate.setMiddleName(middle_init.strip())

			this_inmate.setDaneID(inmate_dict.get('daneID'))
			this_inmate.setBirthYear(inmate_dict.get('BirthYear'))
			this_inmate.setDocID(inmate_dict.get('DOC_ID'))
			this_inmate.setRace(inmate_dict.get('Race'))
			this_inmate.setGender(inmate_dict.get('Gender'))
			
			
			inmates.add(this_inmate)
			
		return inmates

	###
	#	Uses our interface to the inmate data source to get additional inmate data.
	#	Input: a populated InmateCollection
	#	Output: a populated InmateCollection with additional details on each inmate
	##
	def enhanceInmateData (self, inmates):
		global args
		count = 0
		for inmate in inmates:
			count += 1
			if args.verbose >= 3: print("before enhance:", inmate)
			self.inmateRegistryScraper.addEnhancedInmateData(inmate)
			if args.verbose >= 3: print("after  enhance:", inmate)
			if args.verbose >= 1:
				if count%50 == 0: 
					print("Enhanced data on ", count, "people")

		return inmates

	###
	#	Writes out our enhanced inmate data to a CSV.
	#	Input: a populated InmateCollection
	#	Output: void -- except for file system
	##
	def saveInmateData (self, inmates):
		global args
		outputFile = open(args.outfile+".csv", FILE_MODE_WRITE)

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
