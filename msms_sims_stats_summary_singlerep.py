#!/usr/bin/env python

import re 
import sys 

#f=0.5; s=0.1; h=0.5; t=51000; r=1

simsoutfile=sys.argv[1]
fstfile=sys.argv[2]
ihspop2file=sys.argv[3]
xpehhfile=sys.argv[4]
hdhitsfile=sys.argv[5]

f=float(sys.argv[6])
s=float(sys.argv[7])
h=float(sys.argv[8])
t=float(sys.argv[9])
r=sys.argv[10]
seqbp=int(sys.argv[11])

# gets the position of the site under selection
# which is halfway through our sequence
selpos=seqbp/2

#myres=[f,s,h,t,r]
seed=None
accepted=None
frqpop2=None
ddaf=None
fstmax=None
ihsacc=None
ihsv=None
ihsmax=None
xpehhacc=None
xpehhv=None
xpehhmax=None
hd=None

####################################################
file0=open(simsoutfile).readlines()
cmdl=file0[0].split()
seed=int(cmdl[cmdl.index('-seed')+1] )


###########################################

file1=open(fstfile, 'r')
fst={}
for line in file1:  
	x=line.split()
	if not re.search ('fst', line): fst[int(x[0])]=float(x[5])  	
	if not re.search ('pos', line) : 
		if int(x[0]) ==selpos:
			accepted='y'
			frqpop2=x[2]
			ddaf=x[3]
if selpos in fst:  # the site under selection has been accepted by the filter
	for fi in fst: # find the max and see if it is @ position under selection
		if fst[fi]== max(fst.values()) :
			if int(fi)==selpos:
				fstmax='y'
else:
    #print "site filtered out"
    quit()
		
###################################  conta quante volte ihs e max a selpos #####################

file4=open(ihspop2file, 'r') 
ihs2={}
for line in file4:
	x=line.rstrip().split()
	ihs2[int(x[1])]=float(x[-1]) 
	if int(x[1]) ==selpos:
		ihsacc='1'
		ihsv=x[-1]
if selpos in ihs2: 
	for ih in ihs2:
		if ihs2[ih]== max(ihs2.values()) :
			if int(ih)==selpos:
				ihsmax='y'

########################################################################################################

file5=open(xpehhfile, 'r')
xpehh={}
for line in file5:
	x=line.rstrip().split()
	xpehh[int(x[1])]=float(x[-1])
	if int(x[1]) ==selpos:
		xpehhacc='1'
		xpehhv=x[-1]
if selpos in xpehh:
	for xp in xpehh:
		if xpehh[xp]== max(xpehh.values()) :
			if int(xp)==selpos:
				xpehhmax='y'

####################################   conta quante volte hdsite e a selpos0 ###############

file2=open(hdhitsfile, 'r')
count=0
for line in file2: 
	if re.match(str(selpos), line): count+=1

if count>0:
	hd='y'

###################################### print!! ##################################################

myres=[
	f,
	s,
	h,
	t,
	r,
	seed,
	accepted,
	frqpop2,
	ddaf,
	fstmax,
	ihsacc,
	ihsv,
	ihsmax,
	xpehhacc,
	xpehhv,
	xpehhmax,
	hd]

res = []
for x in myres:
	if not x:
		res.append('n')
	else:
		res.append(x)

print "\t".join(['f', 's' ,'h', 't', 'r','seed', 'accepted', 'frqpop2','ddaf', 'fstmax' ,'ihsacc', 'ihs',  'ihsmax', 'xpehhacc', 'xpehh', 'xpehhmax', 'hd'])
print "\t".join(str(i) for i in res)
