import csv
import urllib2

url = 'http://archive.ics.uci.edu/ml/machine-learningdatabases/iris/iris.data'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for rows in cr:
    print rows