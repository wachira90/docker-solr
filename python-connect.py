import requests

url = 'http://192.168.4.42:8983/solr/gettingstarted/select?q.op=OR&q=id%3Aa*&wt=json'
res = requests.get(url)

if res.status_code == 200:
    print('Success!')
elif res.status_code == 404:
    print('Not Found.')

r = res.json()['response']['docs']
print(r)

'''
[{'id': 'adata',
  'compName_s': 'A-Data Technology',
  'address_s': '46221 Landing Parkway Fremont, CA 94538',
  '_version_': 1704089563746533376},
 {'id': 'apple',
  'compName_s': 'Apple',
  'address_s': '1 Infinite Way, Cupertino CA',
  '_version_': 1704089563874459648},
 {'id': 'asus',
  'compName_s': 'ASUS Computer',
  'address_s': '800 Corporate Way Fremont, CA 94539',
  '_version_': 1704089563876556800},
 {'id': 'ati',
  'compName_s': 'ATI Technologies',
  'address_s': '33 Commerce Valley Drive East Thornhill, ON L3T 7N6 Canada',
  '_version_': 1704089563878653952}]
'''
