import urllib2,urllib

def get_redirected_url(url):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url

s="https://www.facebook.com/connect/login_success.html#access_token=AAADyEeX7Ye0BAFQNM8TsJNkhq6jtZABEVtGM0u7Q1oaQLllAIzK1j54O0wDkb81oAYzqYLoRxfnxl8Kgq0VPPpHA2gZBFUTTRnHoZBNtgZDZD&expires_in=6253"

import urllib2, httplib
from urlparse import parse_qs 

args = dict(client_id='266158686822893', redirect_uri='http://simple-galaxy-9806.herokuapp.com/')
"""redirect_url points to */login* URL of our app"""
args["client_secret"] = 'af296f1db1b06e5cb68e719f525a3f21'  #facebook APP Secret
#args["code"] = self.request.get("code")
response = parse_qs(urllib.urlopen(
    "https://graph.facebook.com/oauth/access_token?" +
    urllib.urlencode(args)).read())
print response
#access_token = response["access_token"][-1]

#print access_token

conn = httplib.HTTPSConnection("www.facebook.com")
conn.request("GET", "/dialog/oauth?client_id=266158686822893&client_secret=af296f1db1b06e5cb68e719f525a3f21&redirect_uri=http://simple-galaxy-9806.herokuapp.com&response_type=token")
response = conn.getresponse()
data = response.read()
conn.close()
print data
print response.status
print response.getheaders()


print s.split('#')[1].split('=')[1].split('&')[0]


