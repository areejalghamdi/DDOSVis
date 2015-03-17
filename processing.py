#!/usr/bin/env python
import re
import fileinput
from geoip import geolite2
####################
# must pip install python-geoip to be able to create the json file with the geolocations of ip addresses
# pip install python-geoip-geolite2 
# http://pythonhosted.org/python-geoip/
#####################
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


target = 'TARGETED SERVER'
regex = '(.*) (.*) - \[(.*?)\] "(.*?)" (.*) "(.*?)" "(.*?)" (.*)'
i = 0; 
with open('3300weblogs.json','w') as writeFile:
	writeFile.write('{\n\"nodes\":[\n')
	# the first line is the info of the target
	writeFile.write('\t{\"name\":\"'+ target + '\", \"time\":\"-\", \"request\":\"-\", \"http\":\"-\", \"id\":' +
					 str(i) + ', \"timezone\":\"-\", \"country\":\"US\", \"x\":0, \"y\":0},\n')
	for line in fileinput.input(['www-201501']):
		if(i == 3300):
			break
		m = re.match(regex, line)
		if m:
			address = validate_ip(m.group(1))
			if (address):
				geoloc = geolite2.lookup(m.group(1))
				if geoloc is not None:
					if( i!=0 ): 
						writeFile.write(',\n')
					i+=1
				writeFile.write('\t{\"name\":\"'+ m.group(1) + '\", \"time\":\"'+m.group(3) +'\", \"request\":\"' +
						 m.group(4) + '\", \"http\":\"' + m.group(6) + '\", \"id\":' + str(i) + ', \"timezone\":\"'+ 
						 geoloc.timezone+'\", \"country\":\"'+geoloc.country +'\"'+', \"x\":'+  str(geoloc.location[0]) 
						 +', \"y\":'+  str(geoloc.location[1]) +'}')
	writeFile.write('\n],\n')
	writeFile.write('\"links\":[\n')
 	for k in range(0,i+1):
 		writeFile.write('\t{\"source\":0, ' + '\"target\":' + str(k) +'}')
 		if( k!=i):
 		 writeFile.write(',\n')
 		else:
 		 writeFile.write('\n')
 	writeFile.write(']\n}')

