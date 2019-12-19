from __future__ import print_function
import time, datetime

start_time = datetime.datetime.now()
print("Start Time:", start_time)

from inmate_getter import *
from inmate_registry_scraper import *

inmate_registry_scraper = InmateRegistryScraper()
inmate_getter = InmateGetter(inmate_registry_scraper)

inmate_getter.run()

stop_time = datetime.datetime.now()
duration = stop_time - start_time
print("End   Time:", stop_time)
print ("Total Clock Time in seconds:", duration.total_seconds(), (duration.total_seconds()/60), "min")
