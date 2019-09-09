import sys
import httplib


number = int(sys.argv[1])

conn = httplib.HTTPConnection("18.191.80.4")
conn.request("GET", "/hellohello%d" % number)
res = conn.getresponse()
print res.status, res.reason