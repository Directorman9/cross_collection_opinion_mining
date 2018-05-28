#This Python file uses the following encoding: utf-8
"""
Takes a text file say fileA, for each line(tweet) in fileA remove hashtags, numbers as web links. 

Run it in command line as : python prepro_tweets.py fileA.txt
where fileA is the .txt file containing tweets.
"""

import codecs, sys, nltk, string, glob, os

reload(sys)
sys.setdefaultencoding('utf8')


#Get the command line arguments
inputfile = sys.argv[1]
outputfile = inputfile + '_out.txt'

#Read tweets line by line and pre_process them
with codecs.open(inputfile, mode='r', errors='ignore') as inputFile:
     for line in inputFile:
         if not line.strip(): continue      	
         tokenized = line.split() 
         filtered = filter(lambda x:x[0:4] != 'http' and x[0] != '@' and x[0] != '#' and x[0].isdigit() == False , tokenized)  #Get rid of links, numbers and hashtags    
         joined = " ".join(filtered)
         with codecs.open(outputfile, encoding='utf-8',mode='a', errors='ignore') as outputFile: 
              outputFile.write('%s\n' %(joined))
