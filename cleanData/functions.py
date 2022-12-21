import nltk
import string

def download_required_package():
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('wordnet')
        nltk.download('indian')
    except:
        print("error while downloading nltk package")
download_required_package()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_punctuation(token):
    punct = string.punctuation
    return [i for i in token if i not in punct]

def remove_stop_words(token,sw):
    return list(filter(lambda x: x not in sw,token))

    

def clean_doc(lines):
    lines = lines.lower()
    tokens = word_tokenize(lines)
    stop_words = stopwords.words('english')
    tokens = remove_punctuation(tokens)
    tokens = remove_stop_words(tokens,stop_words)
    return tokens

def test_clean_doc():
    print(clean_doc('hello!, I am pradeep ingle. The words is beautiful'))


