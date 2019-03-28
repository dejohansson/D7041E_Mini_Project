import urllib2
import wget
import os
from HTMLParser import HTMLParser

class parse(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
           for name, value in attrs:
               if name == "href" and value[-3:] == "tgz":
                   print wget.download(repo + value, out=output + "\\" + value)




def createFolder(directory):
    try:
        if not os.path.exists("./" + directory + "/"):
            os.makedirs(directory)
    except OSError:
        pass


parser = parse()

repo="http://www.repository.voxforge1.org/downloads/en/Trunk/Audio/Main/16kHz_16bit/"
output="english"
createFolder(output)
parser.feed(urllib2.urlopen(repo).read())

repo="http://www.repository.voxforge1.org/downloads/fr/Trunk/Audio/Main/16kHz_16bit/"
output="french"
createFolder(output)
parser.feed(urllib2.urlopen(repo).read())

repo="http://www.repository.voxforge1.org/downloads/de/Trunk/Audio/Main/16kHz_16bit/"
output="german"
createFolder(output)
parser.feed(urllib2.urlopen(repo).read())

repo="http://www.repository.voxforge1.org/downloads/es/Trunk/Audio/Main/16kHz_16bit/"
output="spanish"
createFolder(output)
parser.feed(urllib2.urlopen(repo).read())

repo="http://www.repository.voxforge1.org/downloads/pt/Trunk/Audio/Main/16kHz_16bit/"
output="portuguese"
createFolder(output)
parser.feed(urllib2.urlopen(repo).read())


print "end"
