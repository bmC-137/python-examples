#!/usr/bin/python

import urllib2
import urllib

url = "http://172.30.42.127/test.php"
data = {'txtName' : 'Ric', 'txtAge' : '19', 'btnSubmit' : 'Submit'}
params = urllib.urlencode(data)
req = urllib2.Request(url, data=params)
handle = urllib2.urlopen(req)
page = handle.read()
print(page)
