# test of common_word_sequences.py

from common_words_python.common_word_sequences import clean_text
from common_words_python.common_word_sequences import nth_grams
from common_words_python.common_word_sequences import main
from unittest import mock
from unittest.mock import patch, mock_open
import pytest

mock = "this is an This IS An THIS' IS' AN' Is this a mistake, Is this a mistake, There's a problem here, THERE IS A PROBLEM"

def test_clean_text():
    cleaner = clean_text(mock)
    assert cleaner == ['this', 'is', 'an', 'this', 'is', 'an', 'this', 'is', 'an', 'is', 'this', 'a', 'mistake', 'is', 'this', 'a', 'mistake', 'theres', 'a', 'problem', 'here', 'there', 'is', 'a', 'problem']
    return cleaner

def test_nth_grams():
    nth_gram = nth_grams(test_clean_text(), 3)
    assert nth_gram == [('this is an', 3), ('is an this', 2), ('an this is', 2), ('is this a', 2), ('this a mistake', 2), ('is an is', 1), ('an is this', 1), ('a mistake is', 1), ('mistake is this', 1), ('a mistake theres', 1), ('mistake theres a', 1), ('theres a problem', 1), ('a problem here', 1), ('problem here there', 1), ('here there is', 1), ('there is a', 1), ('is a problem', 1)]
    return nth_gram

@patch("builtins.open", mock_open(read_data=mock))
def test_main():
    with open("filename", "r") as f:
        result = f.read()
    open.assert_called_once_with("filename", "r")
    assert result == mock
    final_result = main(result)
    fixed_result = """Sequence Number 1:  this is an - 3
Sequence Number 2:  is an this - 2
Sequence Number 3:  an this is - 2
Sequence Number 4:  is this a - 2
Sequence Number 5:  this a mistake - 2
Sequence Number 6:  is an is - 1
Sequence Number 7:  an is this - 1
Sequence Number 8:  a mistake is - 1
Sequence Number 9:  mistake is this - 1
Sequence Number 10:  a mistake theres - 1
Sequence Number 11:  mistake theres a - 1
Sequence Number 12:  theres a problem - 1
Sequence Number 13:  a problem here - 1
Sequence Number 14:  problem here there - 1
Sequence Number 15:  here there is - 1
Sequence Number 16:  there is a - 1
Sequence Number 17:  is a problem - 1"""
    assert final_result == fixed_result
