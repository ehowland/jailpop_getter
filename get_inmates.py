from __future__ import print_function

from inmate_getter import *
from inmate_registry_scraper import *

inmate_registry_scraper = InmateRegistryScraper()
inmate_getter = InmateGetter(inmate_registry_scraper)

inmate_getter.run()