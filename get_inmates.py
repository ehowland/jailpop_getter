from __future__ import print_function
import time, datetime

start_time = datetime.datetime.now()


from inmate_getter import *
from inmate_registry_scraper import *
from jailpop_args_parse import *

inmate_registry_scraper = InmateRegistryScraper()
inmate_getter = InmateGetter(inmate_registry_scraper)
args = parse_arguments_fix()

inmate_getter.run()

stop_time = datetime.datetime.now()
duration = stop_time - start_time
print ("Total Clock Time in seconds:", duration.total_seconds())
