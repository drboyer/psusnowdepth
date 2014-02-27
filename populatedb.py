#!/usr/bin/python

# Grabs the Walker Building obscard measrements from the past 30 days, and 
#    extracts and saves the snow depth for each day.
#
# This script is meant to be used once to initally populate the database.
import urllib2
import re
from datetime import date, timedelta
import MySQLdb

# Set up db connection
db = MySQLdb.connect(host="localhost",
                     user="USERNAME",
                     passwd="PASSWORD",
                     db="DB_NAME")

cur = db.cursor()                             # Cursor object used to access db



currDate = date.today() - timedelta(days=30)      # Start 30 days ago

for i in range(30):
	# Set up the dates
	dateURLStr = currDate.strftime('%Y%m%d')
	dateDBStr = currDate.strftime('%Y-%m-%d')
	
	# Grab the page
	print "Now processing entry for " + dateDBStr
	page = urllib2.urlopen("http://www.meteo.psu.edu/~wjs1/wxstn/getsummary.php", "dtg="+dateURLStr)
	pagestr = page.read()

	# Extract the snow depth
	rxp = re.search('Snow Depth\s*:\s*([0-9]{1,2}|TRACE)', pagestr)
	rxpMatch= rxp.group(1)
	
	depthstr = -1 if rxpMatch == "TRACE" else rxpMatch      # Traces are -1 in the db, as assigned here.

	# Insert into DB
	try:
		cur.execute("INSERT INTO snowdepth (date, depth) VALUES (%s, %s)", (dateDBStr, depthstr))
		print "Added Entry: " + dateDBStr
	except MySQLdb.Error, e:
        	print "Could not add entry for " + dateDBStr + " to database!"

	# Increment date before looping around again
	currDate = currDate + timedelta(days=1)

