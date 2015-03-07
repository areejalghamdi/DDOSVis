#!/usr/bin/env python
import re
import fileinput
###### TO DO ########
#read in the target from the html page
# upload the file
# read in the file name 
# parse, ignoring the non ip address names
#####################
target = 'TARGETED SERVER'
regex = '(.*) (.*) - \[(.*?)\] "(.*?)" (.*) "(.*?)" "(.*?)" (.*)'
i = 0; 
with open('1500nodes.json','w') as writeFile:
	writeFile.write('{\n\"nodes\":[\n')
	# the first line is the info of the target
	writeFile.write('\t{\"name\":\"'+ target + '\", \"time\":\"-\", \"request\":\"-\", \"http\":\"-\", \"id\":' + str(i) + '},\n')
	
	for line in fileinput.input(['www-201501']):
		if(i == 1500):
			break
		m = re.match(regex, line)
		if m:
			if( i!=0 ): 
				writeFile.write(',\n')
			i+=1
			writeFile.write('\t{\"name\":\"'+ m.group(1) + '\", \"time\":\"'+m.group(3) +'\", \"request\":\"' + m.group(4) + '\", \"http\":\"' + m.group(6) + '\", \"id\":' + str(i) + '}')
	writeFile.write('\n],\n')
	writeFile.write('\"links\":[\n')
 	for k in range(0,i+1):
 		writeFile.write('\t{\"source\":0, ' + '\"target\":' + str(k) +'}')
 		if( k!=i):
 		 writeFile.write(',\n')
 		else:
 		 writeFile.write('\n')
 	writeFile.write(']\n}')