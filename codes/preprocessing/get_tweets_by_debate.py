#This Python file uses the following encoding: utf-8
'''
Gets tweets by hash-tag, separates tweets into differnt files based on their hash-tag (column identification)
*Run this code as: python get_tweets_by_debate.py debates_tweetsfile
where debates_tweetsfile is the file containing raw debate tweets.

*Output is a folder called debate that contains two text files, one containing tweets on Trump and the other on Hillary.

*Author: Hemed Kaporo.
'''

import codecs, sys, csv, os
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputfile = sys.argv[1]
outputDir = "debate/"
if not os.path.exists(outputDir):
   os.makedirs(outputDir)
outputFile1 = os.path.join(outputDir, 'trump.txt')
outputFile2 = os.path.join(outputDir, 'hillary.txt')



with codecs.open(inputfile, encoding='utf-8', mode='r', errors='ignore') as inputFile:
     reader = csv.reader(inputFile, delimiter=',')
     for line in list(reader):
         if line[1] == 'realDonaldTrump' and line[3]=='False':
            with codecs.open(outputFile1 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[2]))
         elif line[1] == 'HillaryClinton' and line[3]=='False':
            with codecs.open(outputFile2 , encoding='utf-8',mode='a', errors='ignore') as outputFile:
                 outputFile.write('%s\n' %(line[2]))
        
          

	     
		
