#!/usr/bin/python

# Grabs the most recent Walker Building obscard measrement, extracts the 
#    snow depth, and writes it to the database
import urllib2
import re
from datetime import date
import MySQLdb

page = urllib2.urlopen("http://www.meteo.psu.edu/~wjs1/wxstn/DATA/current.html")
pagestr = page.read()

rxp = re.search('Snow Depth\s*:\s*([0-9]{1,2})', pagestr)
rxpMatch= rxp.group(1)

depthstr = -1 if rxpMatch == "TRACE" else rxpMatch      # Traces are -1 in the db, as assigned here.


# Get today's date and format it in a form suitable for database insertion
today = date.today()
datestr = today.strftime('%Y-%m-%d')

print "Snow Depth for "+ datestr +": " + depthstr

# Establish the database connection and insert today's snow depth
db = MySQLdb.connect(host="localhost",
		     user="USERNAME",
		     passwd="PASSWORD",
		     db="DB_NAME")
try:
	cur = db.cursor()                             # Cursor object used to access db
	cur.execute("INSERT INTO snowdepth (date, depth) VALUES (%s, %s)", (datestr, depthstr))
	print "Successfully added entry to database."
except MySQLdb.Error, e:
	print "Error adding entry to database."
