# -*- coding: utf-8 -*-
import csv

f = open('fb_friends_initial.txt', 'r')

tocsv = []

for line in f:
	tocsv.append(line.replace(" ",",").replace("-",""))

file = open("fb_friends.csv", "w")
file.write("people_in_pic,friends,gender\n")
for el in tocsv:
	#towrite = ""
	#for i in el:
	#	towrite = towrite + i + ","
	#towrite = towrite + "\n"
	file.write(el)
file.close()

