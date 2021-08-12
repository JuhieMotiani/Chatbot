import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

ps = PorterStemmer()
lemmer = nltk.stem.WordNetLemmatizer()
# Quiet=True is used because we want to download the package quietly, that is without printing any messages on the console
# No message confirming package loading is printed and no errors or warnings are printed if package loading fails
# nltk.download('popular', quiet=True)
# nltk.download('punkt')
# nltk.download('wordnet')

# Lemmatization
def lemtokens(tokens):
    tok = []
    for token in tokens:
        tok.append(lemmer.lemmatize(token))
    return tok

def lemnormalize(text):
    return lemtokens(text)

# user_input = "please get me the ledger balance of Raheja brothers!"


def preprocess(user_input):
    user_input = user_input.lower()
    # ord is the inbuilt function in python which returns unicode value of corresponding character
    # remove punctuation marks if any
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    user_input = user_input.translate(remove_punct_dict)

    # divide the user input into a list of sentences first
    sentence_tokens = nltk.sent_tokenize(user_input)

    # divide the list of sentences into words
    word_tokens = nltk.word_tokenize(user_input)

    # removing stop words
    stop_words = set(stopwords.words('english'))
    word_tokens = [ w for w in word_tokens if not w in stop_words]

    # Stemming
    # word_tokens = [ps.stem(w) for w in word_tokens]

    return lemnormalize(word_tokens)