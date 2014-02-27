psusnowdepth
============

This web page displays snow depth at the Penn State National Weather Service 
co-op site for the current day and the past 30 days (at present). It uses a 
simple Python script to scrape the Snow Depth value off of the online 
observation card and write it to a database.

**Working site:** <http://www.thecloudonline.net/psusnowdepth/>

# How can I fork you and make my own version?

First of all, awesome! Thanks for your interest! You obviously need to set up a
(My)SQL database. The format is super-simple - it's a single table I named
*`snowdepth`* with 3 fields: *`entry_id`*, *`date`* and *`depth`*. 
The first and last fields are `int`s and *`date`* has a `date` type.

The only other package I use you'll need to put on your site is a copy of the
Javascript plotting library [*Flot*] (https://github.com/flot/flot).

