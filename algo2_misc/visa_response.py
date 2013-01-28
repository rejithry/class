import urllib, urllib2

#Define the receipt number and URL
data = urllib.urlencode({'appReceiptNum' : 'wac1208350531'})
req = urllib2.Request("https://egov.uscis.gov/cris/Dashboard/CaseStatus.do", data)

#Execute the post request and fetch the response
response = urllib2.urlopen(req)
the_page = response.read()

#Write the response to a file for better formatting
f = open('f:\\test.txt','w')
f.writelines(the_page)
f.close()

#Read the file and search for the current status
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

f.close()

#Print the status
print vis_response.strip()