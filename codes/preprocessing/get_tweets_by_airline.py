#This Python file uses the following encoding: utf-8
'''
Gets tweets by hash-tag, separates tweets into differnt files based on their hash-tag (column identification)
*Run this code as: python get_tweets_by_airline.py airlines_tweetsfile
where airlines_tweetsfile is the file containing raw airlines tweets.

*Output is a folder called airlies that contains six text files each containing tweets on a particular airline.

*Author: Hemed Kaporo.
'''

import codecs, sys, csv, os
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputfile = sys.argv[1]
outputDir = "airlines/"
if not os.path.exists(outputDir):
   os.makedirs(outputDir)
outputFile1 = os.path.join(outputDir, 'VirginAmerica.txt')
outputFile2 = os.path.join(outputDir, 'United.txt')
outputFile3 = os.path.join(outputDir, 'Southwest.txt')
outputFile4 = os.path.join(outputDir, 'Delta.txt')
outputFile5 = os.path.join(outputDir, 'USAirways.txt')
outputFile6 = os.path.join(outputDir, 'American.txt')



with codecs.open(inputfile, encoding='utf-8', mode='r', errors='ignore') as inputFile:
     reader = csv.reader(inputFile, delimiter=',')
     for line in list(reader):
         if line[5] == 'Virgin America' and line[9]=='0':
            with codecs.open(outputFile1 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[10]))
         elif line[5] == 'United' and line[9]=='0':
            with codecs.open(outputFile2 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[10]))
         elif line[5] == 'Southwest' and line[9]=='0':
            with codecs.open(outputFile3 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[10]))
         elif line[5] == 'Delta' and line[9]=='0':
            with codecs.open(outputFile4, encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[10]))
         elif line[5] == 'US Airways' and line[9]=='0':
            with codecs.open(outputFile5 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[10]))
         elif line[5] == 'American' and line[9]=='0':
            with codecs.open(outputFile6 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[10]))

	     
		
