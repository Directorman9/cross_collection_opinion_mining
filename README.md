# Cross-collection opinion mining

This project contains code and data sets I used in my Master's thesis; Cross-collection aspect based opinion mining using topic models.


How to use these resources.

Datasets:
All data sets can be found under the data sets directory. Detail of data sets can be found in the actual thesis document.

    • The airlines data set can also be downloaded from https://www.kaggle.com/crowdflower/twitter-airline-sentiment
    • The debate data set can also be downloaded from https://www.kaggle.com/benhamner/clinton-trump-tweets
    • The hotels data set can also be downloaded from http://times.cs.uiuc.edu/~wang296/Data 
    • The full movies data set can be downloaded from http://snap.stanford.edu/data/web-Movies.html
    • This phones data set was scraped from gsm-arena.


Codes:
All related code can be found under codes directory. All code is in python. How to use each code is indicated inside the codes. Here we discuss when to use each code.

    1) Preprocessing
    • Run get-hotels_reviews_text.py on the selecting 3 hotels of interest from the downloaded dataset, to get only the text part of the reviews, excluding image and sentiment scored.
    • Run get_tweets_by_airlines.py on the downloaded airlines data set, to get tweets arranged according to the airline of affiliation.
    • Run get_tweets_by_debate.py on the downloaded debate data set, to get tweets arranged according to the candidate of affiliation.
    • Run get_movie_by_id.py on the downloaded movies data set to get movies of interest.
    • Run prepro_tweets.py on the two twitter dataset (airlines and debate) to remove hash tags, web links and numerical values and to put all character to lower case.
    • Run cclda_tam_prepro.py on all the datasets above to make them input ready for the cclda and tam algorithms.
    • Run cptm_prepro.py on all the datasets above to make them input ready for the cptm algorithms.

    2) Run the topic modeling algorithms.
    • Implementation and instructions on cclda and tam can be found from https://github.com/blade091shenwei/TAM_ccLDA
    • Implementation and instructions on cptm can be found from https://github.com/NLeSC/cptm

    
    3) Post process topic modeling outputs.
    • cclda_post_processing.py and tam_post_processing.py post processes cclda and tam outputs, no post processing is required for cptm outputs. Post processing means putting aspect words (nouns) and opinion words (adjectives, verbs, adverbs) in their appropriate places. 
    • cclda_refinement.py, cptm_refinement.py and tam_refinement.py refines the post processed topic modeling outputs. Refinement means taking only those topics that  have highest average pairwise cosine similarity as measured from pre-trained word embeddings of unseen corpus. 

    4) Conduct evaluation
    • coherence measures contain code that was used to measure topic coherence for all the three algorithms outputs.
    • cclda_coherence_measures.py for cclda, cptm_coherence_measures.py for cptm and tam_coherence_measures.py for tam as their named suggest.
    • Measures include lcp, pmi, npmi and cosim. These measures require unseen corpus, in this case wikipedia corpus prepared using code in the side_codes directory.
    • cclda_sentiment_measure.py and cptm_sentiment_measure.py measure sentiment scores of the output opinion words in each perspective and each topic.
    • average_sentiments.py computes the baseline sentiment scores . Run this code on the initial 3 hotels of interest before prepocessing them.
