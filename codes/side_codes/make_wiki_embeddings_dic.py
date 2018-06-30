#This Python file uses the following encoding: utf-8
"""
Takes a file containing embeddings per line i.e. a word and its 300D vector, makes a dictionary and a corpus and save them to disk.
Run it in command line as : python make_wiki_embeddings_dict.py pretrained_embeddings_file
"""
from gensim.corpora.hashdictionary import HashDictionary
import codecs, pickle, sys

reload(sys)
sys.setdefaultencoding('utf8')


#Get the command line arguments
embeddings = sys.argv[1]

#Make the dictionary
import numpy as np
dictionary = {}
with codecs.open(embeddings, encoding='utf-8', mode='r', errors='ignore') as inputFile:
     for line in inputFile:
	 line = line.strip()
	 if not line: continue
	 tokenized = line.split()  
	 word = tokenized[0] 
	 vector = tokenized[-300:]
	 dictionary[word] = vector

#Save dictionary to disk
pickle.dump( dictionary, open( "wiki_embeddings_dic.p", "wb" ) )


'''
dic = pickle.load( open( "wiki_embeddings_dic.p", "rb" ) )
print dic
'''



