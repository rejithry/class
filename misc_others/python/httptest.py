import httplib,ast
from xml.dom.minidom import parseString

access_token="AAAAAAITEghMBADx3WqQQ49rUoRuXzwaeaMOrAffDEKJDu0MqY8yBEV8FGn8DLDWZA9ZBqOb5UZBwDl5M7qZB1YxAZBnxA6tBHIDGaFZCWzFwZDZD"

conn = httplib.HTTPSConnection("graph.facebook.com")
conn.request("GET", "/me/friends?access_token=" + access_token)
response = conn.getresponse()
list_of_friends = ast.literal_eval(response.read())['data']
conn.close()

print len(list_of_friends)

conn = httplib.HTTPSConnection("api.facebook.com")
conn.request("GET", "/method/fql.query?query=SELECT%20uid1,%20uid2%20FROM%20friend%20WHERE%20uid1%20IN%20(SELECT%20uid2%20FROM%20friend%20WHERE%20uid1%20=%20me())%20and%20uid2%20IN%20(SELECT%20uid2%20FROM%20friend%20WHERE%20uid1%20=%20me())&access_token=" + access_token)

response = conn.getresponse()
data = response.read()
conn.close()

dom = parseString(data)

xmlTag = dom.getElementsByTagName('uid1')

print len(xmlTag)


conn = httplib.HTTPSConnection("api.facebook.com")
conn.request("GET", "/method/fql.query?query=SELECT%20uid2%20FROM%20friend%20WHERE%20uid1%20=%20me()%20and%20uid2%20IN%20(SELECT%20uid2%20FROM%20friend%20WHERE%20uid1%20=%20me())&access_token=" + access_token)

response = conn.getresponse()
data = response.read()
conn.close()

dom = parseString(data)

xmlTag = dom.getElementsByTagName('uid2')

print len(xmlTag)

conn = httplib.HTTPSConnection("graph.facebook.com")
conn.request("GET", "/me/friends?access_token=" + access_token)
response = conn.getresponse()
list_of_friends = ast.literal_eval(response.read())['data']
conn.close()

total_friends =  len(list_of_friends)

conn = httplib.HTTPSConnection("api.facebook.com")
conn.request("GET", "/method/fql.query?query=SELECT%20uid1,%20uid2%20FROM%20friend%20WHERE%20uid1%20IN%20(SELECT%20uid2%20FROM%20friend%20WHERE%20uid1%20=%20me())%20and%20uid2%20IN%20(SELECT%20uid2%20FROM%20friend%20WHERE%20uid1%20=%2\
0me())&access_token=" + access_token)

response = conn.getresponse()
data = response.read()
conn.close()

dom = parseString(data)

xmlTag = dom.getElementsByTagName('uid1')

total_neighbor_friends = len(xmlTag)

return_string = "Your total number of neighbors are : " + str(total_friends) + "\n"
return_string = return_string + "Your total number of neighbor friends are : " + str(total_neighbor_friends) + "\n"
return_string = return_string + "Your clustering coefficient is : " + str( (2*total_neighbor_friends*1.0)/(total_friends*(total_friends - 1)) ) + "\n"
print  return_string
