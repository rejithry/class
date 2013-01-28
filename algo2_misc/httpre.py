import httplib, urllib, urllib2
import socket
import HTMLParser
 
 
def httpcon():
    conn = httplib.HTTPConnection("www.python.org:80")
    conn.putrequest("GET", "/index.html")
    agent = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; NeosBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
    conn.putheader('User-Agent', agent)
    #conn.putheader('Accept', 'text/html')
    conn.endheaders()
    r1 = conn.getresponse()
    print r1.status, r1.reason
    conn.close()
def httpcon2(): 
    params = urllib.urlencode({})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain","User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; NeosBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
    conn = httplib.HTTPConnection("www.python.org:80")
    conn.request("GET", "/index.html", params, headers)
    response = conn.getresponse()
    print response
   
 
def get_url(url):
    '''get_url accepts a URL string and return the server response code, response headers, and contents of the file'''
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13',
        'Referer': 'http://python.org'}
    request = urllib2.Request(url, headers=req_headers) # create a request object for the URL
    opener = urllib2.build_opener() # create an opener object
    response = opener.open(request)


c = httplib.HTTPSConnection("egov.uscis.gov")
params = urllib.urlencode({'receipt' : 'wac1208350531' , 'appReceiptNum' : 'wac1208350531'})
c.request("GET", "/cris/Dashboard/CaseStatus.do",params,{})
response = c.getresponse()
#print response.status, response.reason
data = response.read()
#print data

data = urllib.urlencode({'receipt' : 'wac1208350531' , 'appReceiptNum' : 'wac1208350531'})
req = urllib2.Request("https://egov.uscis.gov/cris/Dashboard/CaseStatus.do", data)
response = urllib2.urlopen(req)
#print response.geturl()
#print response.info()
the_page = response.read()

f = open('f:\\test.txt','w')
f.writelines(the_page)
f.close()
printed_lines=-1
start_printing= False
f = open('f:\\test.txt','r')
for i in f:
    if 'Your Case Status' in i:
        start_printing = True;
        printed_lines = printed_lines + 1
    if start_printing and printed_lines != -1:
        printed_lines +=  1
        if printed_lines == 8:
            vis_response = i
            printed_lines = -1
            break
        #print i
        
f.close()

print vis_response.strip()