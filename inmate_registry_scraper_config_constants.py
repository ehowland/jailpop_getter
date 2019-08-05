###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# Configuration and constants for inmate_registry_scraper.
###

TIMEOUT_BETWEEN_REQUESTS = 1 # in seconds

INMATE_REGISTRY_DOMAIN = 'appsdoc.wi.gov'
INMATE_REGISTRY_URL = 'https://appsdoc.wi.gov/lop/home.do'
INMATE_REGISTRY_SEARCH_URL = 'https://appsdoc.wi.gov/lop/searchbasic.do'

DOC_NUMBER_REGEX_PATTERN = 'DOC:\s*<\/SPAN><\/TD>\s*<TD align="Left" nowrap><SPAN class="FormTextData">\s*(\d*)\s*<\/SPAN><\/TD>'
RACE_REGEX_PATTERN = 'Race:\s*<\/SPAN><\/TD>\s*<TD align="Left"><SPAN class="FormTextData">\s*(\w*)\s*<\/SPAN><\/TD>'
SEX_REGEX_PATTERN = 'Sex:\s*<\/SPAN><\/TD>\s*<TD align="Left"><SPAN class="FormTextData">\s*(\w*)\s*<\/SPAN><\/TD>'

#BIRTHDAY_REGEX_PATTERN = 'Race: \s*<\/SPAN><\/TD>\s*<TD align="Left"><SPAN class="FormTextData">\s*(\w*)\s*<\/SPAN><\/TD>'