#This Python file uses the following encoding: utf-8
"""
Takes a folder containing wikipedia folders, which contain wikipedia files, takes documents from each file and add them to a single file. So that we end up with a single file containing all wikipedia articles.
Run it in command line as : python wiki_file_to_file.py dataFolder/
dataFolder is where the folders containing .txt files reside.
"""

import codecs, sys, gensim

reload(sys)
sys.setdefaultencoding('utf8')


#Get the command line arguments
inputFile = sys.argv[1]
outputFile = inputFile + '.txt' 

wordstring = ''
linecount = 0
with codecs.open(inputFile, encoding='utf-8', mode='r', errors='ignore') as inptFile:
     for line in inptFile:
         linecount += 1
	 line = line.strip()
         if not line: continue
         #commaFree = ''.join([ch for ch in line if ch.encode('utf-8') != ',' ])
         wordstring = wordstring + ', ' + line
         
tokenized = wordstring.split(',')
tokenized = [item.strip()  for item in tokenized]
wordfreq = [tokenized.count(w) for w in tokenized] 
dictionary = dict(zip(tokenized, wordfreq))
#print(dictionary.keys())

with codecs.open(outputFile, encoding='utf-8', mode='w', errors='ignore') as outFile:
     outFile.write('Total number of reviews :  %s \n' %(linecount))
     for term in dictionary.keys():
         term = str(term)
         frequency = dictionary[term]
         outFile.write('%s %s \n' %(term, frequency))

