#This Python file uses the following encoding: utf-8
"""
Takes a folder containing wikipedia folders, which contain wikipedia files, takes documents from each file and add them to a single file. So that we end up with a single file containing all wikipedia articles.
Run it in command line as : python wikipedia_files_to_file.py dataFolder/
dataFolder is where the folders containing .txt files reside.
"""

import codecs, sys, nltk, string, glob, os

reload(sys)
sys.setdefaultencoding('utf8')

punctuation1 = """!"#$%&()*+–,-.—*/:;“<=>?@[\]^_”{|}~"""
punctuation2 = """'’`"""

#Get the command line arguments
inputDir = sys.argv[1]

for dir in os.listdir(inputDir):
    directory = os.path.join(inputDir, dir) + '/'
    for file in os.listdir(directory):
        inputFile = os.path.join(directory, file) 
        with codecs.open(inputFile, encoding='utf-8', mode='r', errors='ignore') as inptFile:
	     isArticle = False
	     doc = ""
	     for line in inptFile:
	         line = line.strip()
                 if not line: continue
	         line = line.lower()
	         if isArticle == True:
		    if line[0:6] == '</doc>':
		       puncFree = ''.join([ch if ch.encode('utf-8') not in punctuation1 else ' ' for ch in doc])
		       puncFree = ''.join([ch for ch in puncFree if ch.encode('utf-8') not in punctuation2])
		       tokenized_doc = puncFree.split()
		       with codecs.open("out.txt",encoding='utf-8',mode='a') as outputfile: 
			    for word in tokenized_doc:
			        outputfile.write('%s ' %(word))
			    outputfile.write(str('\n'))		  
		       doc = ""
		       isArticle = False
		    else:
		        doc = doc + " " + line
		 else:
		     if line[0:4] == '<doc':
			isArticle = True     
		     else: continue
