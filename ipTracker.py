#!/usr/bin/python3
import pygeoip
import sys

ip = sys.argv[1]
gi = pygeoip.GeoIP('GeoIP.dat')
giCity = pygeoip.GeoIP('GeoLiteCity.dat')
ctr = gi.country_name_by_addr(ip)
city =  giCity.record_by_addr(ip)
print 'country:'
print ctr
print '*******************************'
print 'city:'
print city