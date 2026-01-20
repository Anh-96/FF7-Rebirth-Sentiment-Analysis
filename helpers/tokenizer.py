import re
from nltk.corpus import stopwords

# Download stopwords once:
# import nltk
# nltk.download("stopwords")

ENGLISH_STOPWORDS = set(stopwords.words("english"))

def tokenize(text):
    """
    Very simple tokenizer: lowercase, split on non-letters, remove stopwords
    :param text: text to tokenize
    :return: list of tokens
    """
    tokens = re.findall(r"\b\w+\b", text.lower())
    return [token for token in tokens if token not in ENGLISH_STOPWORDS and len(token) > 2]


def ngrams(tokens, n=1):
    """
    Build n-grams from a list of tokens
    :param tokens:  to ngrams
    :param n: number of n-grams
    :return: list of n-grams
    """

    return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)] if n > 1 else tokens