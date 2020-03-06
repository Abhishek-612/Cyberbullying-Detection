import json


def clean_data(data):
    o = json.dumps(data)
    x = json.loads(data)

    texts = remove_stopwords(x['text'])
    return texts


def remove_stopwords(text):
    import nltk
    # try:
    #     nltk.data.find('tokenizers/punkt.zip')
    # except LookupError:
    #     nltk.download('punkt')

    stop_list = [word.replace("\n", "") for word in open('datasets/englishstop.txt')]
    texts = [word for word in nltk.word_tokenize(text.lower()) if word not in stop_list and word.isalpha()]

    return texts


clean_data('{"text":"hello, how are you. you fucking whore"}')
