#This Python file uses the following encoding: utf-8
"""
Takes a directory containing files, each file on a specific persepective (product or debate speaker). takes file say fileA, for each line(doc) in fileA tokenises the words, adds a collection number before the line and writes it to an output file. Does the same to all lines(docs) in fileA, and all files in the directory

Run it in command line as : python cclda_tam_prepro.py dataFolder/
dataFolder is the directory containing .txt files each on a specific perspectives.
"""

import codecs, sys, nltk, string, glob, os

reload(sys)
sys.setdefaultencoding('utf8')

punctuation1 = """!"#$%&()*+,-.—*/:;“<=>?@[\]^_”{|}~"""
punctuation2 = """'’`"""

#Get the command line arguments
inputDir = sys.argv[1]
outputFile = inputDir + '_cclda_input'


#Get data in the collections
i=0
for file in os.listdir(inputDir):    
    fileName = file[0:len(file)-4]
    inputFile = os.path.join(inputDir, file) 
    with codecs.open(inputFile, encoding='utf-8', mode='r') as inptFile:
	 for line in inptFile:
             if not line.strip(): continue  #line.strip() returns false if line is empty. 
             doc = line.lower()
     
             #Preprocess the doc
             puncFree = ''.join([ch if ch.encode('utf-8') not in punctuation1 else ' ' for ch in doc])
	     puncFree = ''.join([ch for ch in puncFree if ch.encode('utf-8') not in punctuation2])
             tokenized_doc = puncFree.split()
	     stopWordsFree = [word for word in tokenized_doc if word not in  nltk.corpus.stopwords.words('english')]
	
	     	     
	     #Write the doc to two lines of an output file
	     with codecs.open(outputFile,encoding='utf-8',mode='a') as outputfile: 
		  outputfile.write('%s ' %(i))
                  for term in stopWordsFree:
		      outputfile.write('%s ' %(term))
		  outputfile.write(str('\n'))
    i=i+1      

