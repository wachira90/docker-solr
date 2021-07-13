#!python
import requests
import time
now = time.time()
gg = str(now).replace('.','')
url = 'http://desktop-mke4sph:8983/solr/testdb/update?_='+ str(gg[0:10]) +'&overwrite=true&wt=json'
data='{"add":{ "doc":{"id":"5","fname":"Wachiradd","age":"88"},"boost":1.0,"overwrite":true, "commitWithin": 1000}}'
xx = requests.post(url, headers = headers, data = data)
xx.json()
