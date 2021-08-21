import preprocessing
import io
import random
import string # to process standard python strings
import warnings
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

flag = False
f = open('Data/coffee.txt', 'r', errors = 'ignore')
raw = f.read()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = preprocessing.preprocess(raw)

greetings = ("hello", "hi", "greetings", "hey")
greeting_response = "Hello I am AlphaCharlie. I really love Coffee. You can ask me anything about it!"

endwords = ("bye", "take care", "thank you", "see you")

def response(user_response):
    flag=False
    if user_response.lower() in greetings:
        flag = True
        return greeting_response
    
    elif user_response.lower() in endwords:
        return "Bye!"
        
    else:
        robo_response=''
        sent_tokens.append(user_response)
        TfidfVec = TfidfVectorizer(tokenizer=preprocessing.lemnormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if(req_tfidf==0):
            robo_response=robo_response+"I am sorry! I don't understand you"
            return robo_response
        else:
            robo_response = robo_response+sent_tokens[idx]
            sent_tokens.remove(user_response)
            return robo_response
        
