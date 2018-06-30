#This Python file uses the following encoding: utf-8
"""
Takes a file containing articles per line, makes a dictionary and a corpus and save them to disk.
Run it in command line as : python save_dictionary_to_disk.py datafile
datafile is the file containing articles per line example wikipedia articles.
"""
from gensim.corpora.hashdictionary import HashDictionary
import codecs, pickle, sys

reload(sys)
sys.setdefaultencoding('utf8')


#Get the command line arguments
inputFile = sys.argv[1]

doc=[]
texts=[]
with codecs.open(inputFile, encoding='utf-8', mode='r', errors='ignore') as inptFile:
     for line in inptFile:
         line = line.split()
         for word in line:
             doc.append(word)
         texts.append(doc)
         doc=[]

dictionary = HashDictionary(texts)
w2id = dictionary.token2id
corpus = [dictionary.doc2bow(doc) for doc in texts]
pickle.dump( dictionary, open( "wiki_dictionary.p", "wb" ) )
pickle.dump( w2id, open( "wiki_w2id.p", "wb" ) )
pickle.dump( corpus, open( "wiki_corpus.p", "wb" ) )


'''
dic = pickle.load( open( "wiki_dictionary.p", "rb" ) )
w2id = pickle.load( open( "wiki_w2id.p", "rb" ) )
data = pickle.load( open( "wiki_corpus.p", "rb" ) )
print w2id
print data
'''



