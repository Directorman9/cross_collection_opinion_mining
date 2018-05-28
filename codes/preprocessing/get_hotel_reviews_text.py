#This Python file uses the following encoding: utf-8
'''
Gets only text content of the hotel review, it excludes sentiment score, image tags etc.
Author: Hemed Kaporo.
'''

import codecs, sys, os
reload(sys)
sys.setdefaultencoding('utf8')

#Get the command line arguments
inputDir = sys.argv[1]
outputDir = inputDir + '_outputs/'
if not os.path.exists(outputDir):
   os.makedirs(outputDir)


#Get data in the collections
for file in os.listdir(inputDir):
    inputfile = os.path.join(inputDir, file) 
    outputfile = os.path.join(outputDir, file)
    with codecs.open(inputfile, encoding='utf-8', mode='r') as inputFile:
         for line in inputFile:
             if not line.strip(): continue
             if line[0:9] == '<Content>':                
	        with codecs.open(outputfile,encoding='utf-8',mode='a') as outputFile: 
                     outputFile.write(line[9:len(line)])
	     
		

