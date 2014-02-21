import urllib2


def getSourceFromURL(URL):
        user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/$'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(URL, None, headers)
        response = urllib2.urlopen(req)
        return response.read()
def findChar(s, ges, pos):
	counter = 0
	for i,c in enumerate(s):
		#print i, ":", c
		if ges is c: 
			counter = counter + 1
			if counter == pos:
				return i	
	return -1
source = getSourceFromURL("http://www.wieistmeineip.de")
splited = source.split("<div class=\"title\"")
line = splited[1].split("\n")[0]

# print findChar(line, '>', 2) , ":" , findChar(line, '<', 2)
ip = line[findChar(line, '>', 2)+1:findChar(line, '<', 2)]

location_split = source.split("<div class=\"location\"")
location_line = location_split[1].split("\n")[0]
location = location_line[findChar(location_line, '"', 3) + 1: findChar(location_line, '"', 4)]


print "------------------------------------------"
print "\n"
print "Location: ", location
print "IP: ", ip
print "\n"
print "------------------------------------------"
