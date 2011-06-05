import sys
import csv
import urllib2
import ConfigParser
from datetime import datetime
from lxml import etree

def settings(section, cfgfile='pfupload.cfg'):
	config = ConfigParser.ConfigParser()
	config.read(cfgfile)
	return dict(config.items(section))

# validation needed here
INPUTFILE = sys.argv[1]
KEY = sys.argv[2]
USER = settings('user')
ORG = settings('org')
NS = "http://zesty.ca/pfif/1.1"
PFIF = "{%s}" % NS
NSMAP = {'pfif' : NS}

def upload_to_pf(url, key, xmldata):
	url += "/api/write?key=" + key
	req = urllib2.Request(url=url, 
	                      data=xmldata, 
	                      headers={'Content-Type': 'application/xml'})
	response = urllib2.urlopen(req)
	return response.read()

root = etree.Element(PFIF + "pfif", nsmap=NSMAP)
reader = csv.reader(open(INPUTFILE))

firstrow = reader.next()
columns = dict([(n.strip(),i) for i,n in enumerate(firstrow)])
for i, row in enumerate(reader):
	if row:
		person = etree.SubElement(root, PFIF+"person", nsmap=NSMAP)
		pid = ORG['domain'] + '/'+ str(i+1)
		etree.SubElement(person, PFIF+'person_record_id', nsmap=NSMAP).text = pid
		for k,v in USER.iteritems():
			etree.SubElement(person, PFIF+k, nsmap=NSMAP).text = v
		for name, index in columns.iteritems():
			etree.SubElement(person, PFIF+name, nsmap=NSMAP).text = row[index]

xml = etree.tostring(root)
print(etree.tostring(root, pretty_print=True))
resp = upload_to_pf(ORG['targeturl'] ,KEY, xml) 
print resp