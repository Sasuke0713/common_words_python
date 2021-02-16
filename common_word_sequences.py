import sys
import os
import collections
import re
import nltk
import string
from multiprocessing import Pool

def clean_text(text):
    """Clean text of any punctuation and ensure to split on whitespace
    We want to take punctuation out so punctuation doesn't affect our count for the same words 
    along with making all text the same size"""

    # Remove punctuations etc and split on whitespace https://towardsdatascience.com/cleaning-text-data-with-python-b69b47b97b76
    text = text.lower()
    text = text.encode('ascii', 'ignore').decode()
    text = re.sub(r'http*\S+', ' ', text)
    text = re.sub(r'@\S+', ' ', text)
    text = re.sub(r'#\S+', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    return text

def nth_grams(text, n):
    """ This Function allows computing unigram(1), bigram(2), trigam(3) etc. 
    Basically a unigram is a one word sequence and so on. 
    It will take the list of text and compute Nth number of sequences you want from the text
    Then use collections to count the 100 most common"""

    # http://www.locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    ngram = zip(*[text[i:] for i in range(n)])
    word_sequences = (' '.join(word) for word in ngram)

    # https://www.guru99.com/python-counter-collections-example.html
    output = collections.Counter(word_sequences)
    return output.most_common(100)

path_files: str = sys.argv[1:]

def main(path_files):
    """
    Main function for script to collect args, pass to configuration function, and then create EMR
    :return: None
    """

    if not path_files:
      path_files = ["/dev/stdin"]

    with open(path_files) as input:
      text = input.read()
      mr_clean = clean_text(text)
      better_format = '\n'.join('Sequence Number {}: {}'.format(*k) for k in enumerate(nth_grams(mr_clean, 3), start = 1))
      replace_comma = re.sub(',', '-', better_format)
      replace_single_quote = re.sub("'", ' ', replace_comma)
      output = re.sub("[()]", '', replace_single_quote)
      return output

if __name__=='__main__':
  # Probably a lot better ways to do this but from my understanding python has a GIL which does not allow real multi threading
  # https://medium.com/python-experiments/parallelising-in-python-mutithreading-and-mutiprocessing-with-practical-templates-c81d593c1c49
  with Pool(os.cpu_count() - 1) as pool: # Create a multiprocessing Pool
    for result in pool.map(main, path_files):
      print(result, '\n')
