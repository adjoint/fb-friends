import csv

with open('my_fb_friends_initial.csv', 'rb') as f:
    reader = csv.reader(f)
    fbf = map(list, reader)
del fbf[0]  

file = open("my_fb_friends.csv", "w")
file.write("people_in_pic,friends,gender\n")
for el in fbf:
	towrite = ""
	for i in el:
		towrite += i + ","
	file.write(towrite.replace(" ","")[:-1]+"\n")
file.close()

