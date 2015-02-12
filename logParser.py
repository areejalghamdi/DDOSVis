#!/usr/bin/env python
import re

line = 'sol-fttb.154.122.119.46.sovam.net.ua www.cs.uoregon.edu - [01/Jan/2015:00:00:18 -0800] "GET /research/paracomp/papers/ijhpca05.tau/ijhpca_tau.pdf HTTP/1.1" 200 1288301 "http://www.cs.uoregon.edu/research/paracomp/papers/ijhpca05.tau/ijhpca_tau.pdf"'
regex = '(.*) (.*) - \[(.*?)\] "(.*?)"'
m = re.match(regex, line)
#m = re.findall(r'\"(.*?)\"', line)
#m = re.findall(r'.*', line)
if m:
	print m.group()