#This Python file uses the following encoding: utf-8
"""
Takes a directory containing files, each file on a specific persepective (product or debate speaker). Takes a file say fileA, for each line(doc) in fileA takes only nouns(topic words) and list them as a first line of another text file say fileB, then takes adjectives, adverbs and pronouns (opinion words) from fileA and lists them as the second line in fileB. Does the same to all lines(docs) in fileA. and all files in the directory.

Run it in command line as : python cptm_prepro.py dataFolder/
dataFolder is the directory containing .txt files each on a specific perspectives.
"""

import codecs, sys, nltk, string, glob, os

reload(sys)
sys.setdefaultencoding('utf8')

punctuation1 = """!"#$%&()*+,-.—*/:;“<=>?@[\]^_”{|}~"""
punctuation2 = """'’`"""

#Get the command line arguments
inputDir = sys.argv[1]
outputParentDir = inputDir + '_perspectives/'
if not os.path.exists(outputParentDir):
   os.makedirs(outputParentDir)


#Get data in the collections
for file in os.listdir(inputDir):
    fileName = file[0:len(file)-4]
    outputDir = os.path.join(outputParentDir, fileName)  
    if not os.path.exists(outputDir):
           os.makedirs(outputDir)
    inputFile = os.path.join(inputDir, file) 
    with codecs.open(inputFile, encoding='utf-8', mode='r') as inptFile:
	 i=0
	 for line in inptFile:
             if not line.strip(): continue
             doc = line.lower()
     
             #Preprocess the doc
             puncFree = ''.join([ch if ch.encode('utf-8') not in punctuation1 else ' ' for ch in doc])
	     puncFree = ''.join([ch for ch in puncFree if ch.encode('utf-8') not in punctuation2])
             tokenized_doc = puncFree.split()
	     stopWordsFree = [word for word in tokenized_doc if word not in  nltk.corpus.stopwords.words('english')]
	     POS_tagged = nltk.pos_tag(stopWordsFree)


             #Get topic words(nouns) and opinion words separately
             nouns_tags = ['NN','NNS','NNP','NNPS']
             opinion_tags = ['JJ','JJR','JJS','RB','RBR','RBS','RP','VB','VBD','VBG','VBN','VBZ']
             topic_words = [term[0] for term in POS_tagged if term[1] in nouns_tags] 
	     opinion_words = [term[0] for term in POS_tagged if term[1] in opinion_tags]
	     
	     
	     #Write the doc to two lines of an output file
             outputfile = "doc" + str(i) + ".txt"
             outputFile = os.path.join(outputDir, outputfile)
	     with codecs.open(outputFile,encoding='utf-8',mode='w') as outputfile: 
		  for term in topic_words:
		      outputfile.write('%s ' %(term))
		  outputfile.write(str('\n'))
		  for term in opinion_words:
                      outputfile.write('%s ' %(term))
             i=i+1

