Copyright 2019 Corin Buchanan-Howland


## Overview ##

Inmate getter: takes a list of inmates and pulls additional data from Wisconsin's Offender Locator at https://appsdoc.wi.gov/lop/home.do.

Setup:

0) install the requests module for Python 2.7, using this command: python.exe -m pip install requests
1) extract all python files into a single directory.
2) edit constants files as needed, especially image_getter_config_constants.py
3) create a CSV of the inmates you want to look up following the format from ^
4) run get_inmates.py
5) view your output CSV at the location you specified in image_getter_config_constants.py.

Known issues:
* Does not currently handle cases with multiple results
* Birthdays are not available, so are disabled
* Very little error handling

## License ##

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

This program should only be used in compliance with the terms and conditions of any third-party applications or servers that the
program may be configured to interact with, and with any local laws. The author takes no responsibility for any use that involves
criminal activity or misconduct.