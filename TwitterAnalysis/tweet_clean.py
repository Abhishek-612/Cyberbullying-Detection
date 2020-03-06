import json

def clean_data(data):
    o = json.dumps(data)
    x = json.loads(data)

    text = x['text']

    texts = remove_stopwords(text)
    print(texts)


def remove_stopwords(text):
    import nltk
    nltk.download('punkt')

    stoplist = [word.replace("\n", "") for word in open('englishstop.txt')]
    texts = [word for word in nltk.word_tokenize(text.lower()) if word not in stoplist and word.isalpha()]

    return texts
