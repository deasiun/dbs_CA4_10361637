# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:20:23 2017

@author: Des McCann
DBS ID  #10361637

Using dictionaries to complete this exercise
Importing RE really to get some additional character finding functionality
Importing csv to enable the output of a CSV
To get this working on any computer you will need to update read in file location and the output file location.
the read in is controlled in Line 32 -->  textin = open('d:\\dbsc\\database\\changes_python.log.txt').readlines()
the output is controlled by  Line 28/29 -->outfile = open("d:\\dbsc\\database\\CA4LogsOut.csv","w")
"""


import re #to use special character - just trying it out
import csv
#defining my dicttionary
mydictionary = dict()
mydictionary['userid'] =0
mydictionary['user'] = ""
mydictionary['datetime']="2000-01-01"
mydictionary['CountA']= 0
mydictionary['CountD']= 0
mydictionary['CountM']= 0
mydictionary['comment'] =''
outfile =open("d:\\dbsc\\database\\CA4LoggOut.csv","w") 
outputfile = csv.writer(outfile)
startloop=0 # to get rid of the default printout first time through

countloop=0 # count the value add loop
textin = open('d:\\dbsc\\database\\changes_python.log.txt').readlines()

listofstarts=['A','M','D','--------------------------','Changed'] #this is a list of things that can start of a line
#print mydictionary.keys() #the keys are the individual names in the dictionary ie the first name of each pair)
mykeylist = ()
mykeylist = mydictionary.keys()
outputfile.writerow(mykeylist) #this sends a header lis to the csv file.

def fncount(textin):#count the loop length
    countall=0   
    for line in textin:
         countall = countall+1 # read in a line  & increment loop counter
    return countall
    
def loopbuild(textin):#count each transaction
    countlp=0
    startlp=0
    for line in textin:
            if startlp==0:
                startlp=1 #first line in the logs is noise this deals with it
                continue
            elif  "------------------------------------" in line:
                countlp=countlp+1
    return countlp

#print "check loop count matches", fncount(textin)
#print "check transaction counter logic", loopbuild(textin)

#back to main query builder
for line in textin:
    if startloop==0:
        startloop=1 #first line in the logs in noise this deals with it
        continue
    elif "------------------------------------" in line:
        mylist = ()
        mylist = mydictionary.values()
        outputfile.writerow(mylist)#wite the previous set of values out before resetting all values
        mydictionary = dict()
        mydictionary['userid'] =0
        mydictionary['user'] = ""
        mydictionary['datetime']="2000-01-01"
        mydictionary['CountA']= 0
        mydictionary['CountD']= 0
        mydictionary['CountM']= 0
        mydictionary['comment'] =''
        countloop=countloop+1
    elif re.search('^r1',line):
#        print line
        line=line.rstrip() # strip out hte space
        word=line.split("|") # use the pipe as the delimiter
        mydictionary['userid'] =word[0]
        mydictionary['user']=word[1]
        datestamp=word[2]
        pieces=datestamp.split(" +")
        mydictionary['datetime']=pieces[0]
    elif re.search('^   A',line):
        mydictionary['CountA']= mydictionary['CountA']+1
    elif re.search('^   M',line):
        mydictionary['CountM']= mydictionary['CountM']+1
    elif re.search('^   D',line):
        mydictionary['CountD']= mydictionary['CountD']+1
    else:
        #to distinguish between  comments a list was built of possible ways to start - if not on the list then it must be a comment
        linez=line.strip()
        wordz=linez.split()
        try:
            if wordz[0] not in listofstarts:
                mydictionary['comment'] =linez
        except:
            continue

outfile.close()

