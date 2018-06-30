#This Python file uses the following encoding: utf-8
"""
Calculates avarage sentiment score for every aspect from a given hotel review dataset.

Run it in command line as : python ground_truth_sentiments.py hotel_review_file

"""

import codecs, sys, glob, os
from shutil import copyfile

reload(sys)
sys.setdefaultencoding('utf8')


#Get the command line arguments
inputDir = sys.argv[1]
outputDir = inputDir + '_outputs/'
if not os.path.exists(outputDir):
   os.makedirs(outputDir)


#Get data in the hotel review file
for file in os.listdir(inputDir): 
    aspects = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]   
    normalized = []
    inputFile = os.path.join(inputDir, file) 
    outputfile = os.path.join(outputDir, file)
    with codecs.open(inputFile, encoding='utf-8', mode='r') as inptFile:
         for line in inptFile:   
             line = line.strip()
             if line[0:7] == '<Value>' and line[7] != '-': 
                rating = float(line[7:])
                aspects[0][0] = aspects[0][0] + rating
                aspects[0][1] = aspects[0][1] + 1
             elif line[0:7] == '<Rooms>' and line[7] != '-':
                  rating = float(line[7:])
                  aspects[1][0] = aspects[1][0] + rating
                  aspects[1][1] = aspects[1][1] + 1
             elif line[0:10] == '<Location>' and line[10] != '-':
                  rating = float(line[10:])
                  aspects[2][0] = aspects[2][0] + rating
                  aspects[2][1] = aspects[2][1] + 1
             elif line[0:13] == '<Cleanliness>' and line[13] != '-':
                  rating = float(line[13:])
                  aspects[3][0] = aspects[3][0] + rating
                  aspects[3][1] = aspects[3][1] + 1
             elif line[0:23] == '<Check in / front desk>' and line[23] != '-':
                  rating = float(line[23:])
                  aspects[4][0] = aspects[4][0] + rating
                  aspects[4][1] = aspects[4][1] + 1 
             elif line[0:9] == '<Service>' and line[9] != '-':
                  rating = float(line[9:])
                  aspects[5][0] = aspects[5][0] + rating
                  aspects[5][1] = aspects[5][1] + 1                        
             elif line[0:18] == '<Business service>' and line[18] != '-':
                  rating = float(line[18:])
                  aspects[6][0] = aspects[6][0] + rating
                  aspects[6][1] = aspects[6][1] + 1

    #normalize sentiments from 1->5 to -1->1.
    for aspect in  aspects:
        value = ((aspect[0]/aspect[1]) / 2) - 1.5
        normalized.append(value)

    #print results
    with codecs.open(outputfile,encoding='utf-8',mode='w') as outputFile: 
         outputFile.write('Value : %s \n' %(normalized[0]))
         outputFile.write('Rooms : %s \n' %(normalized[1]))
         outputFile.write('Location : %s \n' %(normalized[2]))
         outputFile.write('Cleanliness : %s \n' %(normalized[3]))
         outputFile.write('front desk : %s \n' %(normalized[4]))
         outputFile.write('Service : %s \n' %(normalized[5]))
         outputFile.write('Business service : %s \n' %(normalized[6]))
		
                
           
