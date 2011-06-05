## Requirements

	Python 2.7+ 
	OR 
	any x86 operating system (for the executable)

## Install

[Download](https://bitbucket.org/gallipoli/pfupload/downloads)

Simply download and extract the zip file. The zip file contains the necessary executable and configuration file.

Alternatively, download the script itself (pfupload.py) and the configuration file, and simply run it as a standalone python module. 

## Usage 

Use pfupload.cfg to set up which organization to use and user information. Then simply run this on the command line, inserting your csv file and API key.

	python pfupload.py [CSVFILE] [APIKEY]

If you don't have python, you can use the executable provided (created with cx_freeze). If you are on Windows, you may need to rename it to "pfupload.exe"

	pfupload [CSVFILE] [APIKEY]

The script is expecting a CSV file with the first row containing columns that correspond to the PFIF standard. Here are the basic person entities supported:

	full_name	(REQUIRED)
	source_name
	source_date
	source_url
	first_name
	last_name
	sex
	date_of_birth
	age
	home_street
	home_neighborhood
	home_city
	home_state
	home_postal_code
	home_country
	photo_url
	other

## Troubleshooting

The tool requires the following

*	An internet connection to upload
*	A filled in config file
*	A CSV that contains at least full_name

The script outputs the XML file it is sending and the response it gets back from the server. Some troubleshooting steps:

*	Check the XML file. Compare it to the example [here](http://zesty.ca/pfif/1.2/pfif-1.2-example.html). If the values in the CSV contain non-supported characters, that could be the problem.

*	Check the response from the server. Details on what that response means can be found [here](http://code.google.com/p/googlepersonfinder/wiki/DataAPI) in the "Uploading data into Person Finder" section.

## Issues

Because of the nature of the executable creator (cx_Freeze), I was unable to get an x64 version working for Windows.