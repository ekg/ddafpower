#!/usr/bin/env python

import sys
import re

myphysicalpositions=sys.argv[1]
#myphysicalpositions  contains pyisical positions in the firs column and has a header

myfile=open(myphysicalpositions).readlines()
positions=[x.rstrip().split()[1:]  for x in myfile  if re.match('positions', x)][0]
cmdl=myfile[0].split()
sizebp=int(cmdl[cmdl.index('-r') +2] )

count=0
recrate=1.6*10**-8
mygeneticposstart=0 
# transform into physical positions
positions = [int(round(float(x)*float(sizebp))) for x in positions]
mystart=0
count=1
#print 'rs%s %s %.10f a b' %(count, mystart, mygeneticposstart )
for position in positions:
	physicaldistance=position-mystart
	myincrement=physicaldistance*recrate
	mygeneticposition=mygeneticposstart+myincrement
	print 'rs%s %s %.10f a b' %(count, position, mygeneticposstart )
	mystart=position
	mygeneticposstart=mygeneticposition
	count += 1
