# coding=utf-8
#!/usr/bin/env python

import os
import csv
import random
import string


def get_file_path(filename):
	currentdirpath = os.getcwd()
	file_path = os.path.join(currentdirpath, filename)
	# print file_path
	return file_path

path = get_file_path('Employeeuser.csv')


def get_randomstrig():
	rnstring=''
	for i in range(0,3):
		# print i
		rnstring += random.choice(string.ascii_letters)
		# print rnstring
	return rnstring


def read_csv(filepath):
	userfake = {}
	i = 0
	with open(filepath,'r') as csvfile:
		reader = csv.reader(csvfile)
		# print reader
		for row in reader:
			if '1' in row[1]:
				# print row[0], row[1],row[2]
				newword = row[1]
				# print newword
				prefix1, num1 = newword[:6], newword[6:]
				# print(prefix1,num1)
				fakeuserid = prefix1+get_randomstrig()+num1
				# print fakeuserid

				i += 1
				userfake[i] = fakeuserid
				# print userfake[i]


			# elif '0' in row[2]:
			# 	print row[5]
	# print userfake
	return userfake

# read_csv(path)


def get_winner():
	userfakeraj = read_csv(path)
	print len(userfakeraj)
	# for i in range(1,len(userfakeraj)+1):
	for i in range (1,40):
			print userfakeraj[i]

	ran_num = random.randint(0,len(userfakeraj)-1)
	winner = userfakeraj[ran_num]
	print "And the winner of the userid is %s %s" %(winner, ran_num)

get_winner()