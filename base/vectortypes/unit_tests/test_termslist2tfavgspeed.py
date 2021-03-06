#
#    Unit Test for html2vect.base.vectortypes.string2tf
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import sys
sys.path.append('../../../../')

import unittest
import numpy as np
import scipy.sparse as ssp
from html2vect.base.termstypes.cngrams import String2CNGramsList
from html2vect.base.termstypes.wngrams import String2WNGramsList
from html2vect.base.vectortypes.termslist2tfavgspeed import trms2tfspd_dict

class Test_BaseString2TF(unittest.TestCase):
    
    def setUp(self):
        
        self.s2ngl_c3grams = String2CNGramsList(n=3)
        self.s2ngl_words = String2WNGramsList(n=1)
        self.s2ngl_w3grams = String2WNGramsList(n=3)
        
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"

        self.txt_sample = "This This This aaa is a unit test for html2tfd.charngrams.BaseString2TF class aaa for html2vectors package/module"

        #I could have the list of Char-3-grams and Word-3-grams, and/or Word-unigrams. 
        #However the above string will be conveted first to the proper terms list which is the functions' input.

        #Terms-Indexs Vocabulary 
        self.c3grams_tid_vocab = { 
            ' a ' : 0, ' cl' : 1, ' fo' : 2, ' ht' : 3, ' is' : 4, ' pa' : 5,\
            ' te' : 6, ' un' : 7, '.Ba' : 8, '.ch' : 9, '/mo' : 10, '2TF' : 11,\
            '2tf' : 12, '2ve' : 13, 'Bas' : 14, 'F c' : 15, 'Str' : 16, 'TF ' : 17,\
            'Thi' : 18, 'a u' : 19, 'ack' : 20, 'age' : 21, 'ams' : 22, 'arn' : 23,\
            'ase' : 24, 'ass' : 25, 'cha' : 26, 'cka' : 27, 'cla' : 28, 'cto' : 29,\
            'd.c' : 30, 'dul' : 31, 'e/m' : 32, 'eSt' : 33, 'ect' : 34, 'est' : 35,\
            'fd.' : 36, 'for' : 37, 'g2T' : 38, 'ge/' : 39, 'gra' : 40, 'har' : 41,\
            'his' : 42, 'htm' : 43, 'ing' : 44, 'is ' : 45, 'it ' : 46, 'kag' : 47,\
            'l2t' : 48, 'l2v' : 49, 'las' : 50, 'ml2' : 51, 'mod' : 52, 'ms.' : 53,\
            'ng2' : 54, 'ngr' : 55, 'nit' : 56, 'odu' : 57, 'or ' : 58, 'ors' : 59,\
            'pac' : 60, 'r h' : 61, 'ram' : 62, 'rin' : 63, 'rng' : 64, 'rs ' : 65,\
            's a' : 66, 's f' : 67, 's i' : 68, 's p' : 69, 's.B' : 70, 'seS' : 71,\
            'ss ' : 72, 'st ' : 73, 't f' : 74, 't t' : 75, 'tes' : 76, 'tfd' : 77,\
            'tml' : 78, 'tor' : 79, 'tri' : 80, 'ule' : 81, 'uni' : 82, 'vec' : 83\
        }

        self.c3grams_tid_vocab_small = { 
            ' a ' : 0, ' cl' : 1, ' fo' : 2, ' ht' : 3, ' is' : 4, ' pa' : 5,\
            ' te' : 6, ' un' : 7, '.Ba' : 8, '.ch' : 9, '/mo' : 10, '2TF' : 11,\
            '2tf' : 12, '2ve' : 13, 'Bas' : 14, 'F c' : 15, 'Str' : 16, 'TF ' : 17,\
            'Thi' : 18, 'a u' : 19, 'ack' : 20, 'age' : 21, 'ams' : 22, 'arn' : 23,\
            'ase' : 24, 'ass' : 25, 'cha' : 26, 'cka' : 27, 'cla' : 28, 'cto' : 29,\
            'd.c' : 30, 'dul' : 31, 'e/m' : 32, 'eSt' : 33, 'ect' : 34, 'est' : 35,\
            'fd.' : 36, 'for' : 37, 'g2T' : 38, 'ge/' : 39, 'gra' : 40, 'har' : 41,\
            'his' : 42, 'htm' : 43, 'ing' : 44, 'is ' : 45, 'it ' : 46, 'kag' : 47,\
            'l2t' : 48, 'l2v' : 49, 'las' : 50, 'ml2' : 51, 'mod' : 52, 'ms.' : 53,\
            'ng2' : 54, 'ngr' : 55, 'nit' : 56, 'odu' : 57, 'or ' : 58, 'ors' : 59,\
            'pac' : 60,\
        }

        self.c3grams_tid_vocab_large = { 
            ' a ' : 0, ' cl' : 1, ' fo' : 2, ' ht' : 3, ' is' : 4, ' pa' : 5,\
            ' te' : 6, ' un' : 7, '.Ba' : 8, '.ch' : 9, '/mo' : 10, '2TF' : 11,\
            '2tf' : 12, '2ve' : 13, 'Bas' : 14, 'F c' : 15, 'Str' : 16, 'TF ' : 17,\
            'Thi' : 18, 'a u' : 19, 'ack' : 20, 'age' : 21, 'ams' : 22, 'arn' : 23,\
            'ase' : 24, 'ass' : 25, 'cha' : 26, 'cka' : 27, 'cla' : 28, 'cto' : 29,\
            'd.c' : 30, 'dul' : 31, 'e/m' : 32, 'eSt' : 33, 'ect' : 34, 'est' : 35,\
            'fd.' : 36, 'for' : 37, 'g2T' : 38, 'ge/' : 39, 'gra' : 40, 'har' : 41,\
            'his' : 42, 'htm' : 43, 'ing' : 44, 'is ' : 45, 'it ' : 46, 'kag' : 47,\
            'l2t' : 48, 'l2v' : 49, 'las' : 50, 'ml2' : 51, 'mod' : 52, 'ms.' : 53,\
            'ng2' : 54, 'ngr' : 55, 'nit' : 56, 'odu' : 57, 'or ' : 58, 'ors' : 59,\
            'pac' : 60, 'r h' : 61, 'ram' : 62, 'rin' : 63, 'rng' : 64, 'rs ' : 65,\
            's a' : 66, 's f' : 67, 's i' : 68, 's p' : 69, 's.B' : 70, 'seS' : 71,\
            'ss ' : 72, 'st ' : 73, 't f' : 74, 't t' : 75, 'tes' : 76, 'tfd' : 77,\
            'tml' : 78, 'tor' : 79, 'tri' : 80, 'ule' : 81, 'uni' : 82, 'vec' : 83,\
            'aaa' : 84, 'bbb' : 85, 'ccc' : 86, 'ddd' : 87, 'eee' : 88, 'fff' : 89,\
            'ggg' : 90, 'hhh' : 91, 'iii' : 92, 'jjj' : 93, 'kkk' : 94, 'lll' : 95\
        }

        self.words_tid_vocab = {
            'a': 1, 'for': 2, 'This': 3, 'is': 4, 'html2vectors': 5, 'test': 6,\
            'package/module': 7, 'html2tfd.charngrams.BaseString2TF': 8, 'class': 9, 'unit': 10\
        }

        self.words_tid_vocab_small = {
            'a': 1, 'for': 2, 'This': 3, 'is': 4, 'html2vectors': 5, 'test': 6,\
            'package/module': 7\
        }

        self.words_tid_vocab_large = {
            'a': 1, 'for': 2, 'This': 3, 'is': 4, 'html2vectors': 5, 'test': 6,\
            'package/module': 7, 'html2tfd.charngrams.BaseString2TF': 8, 'class': 9,\
            'unit': 10, 'aaaword': 11, 'bbbword': 12, 'cccword': 13, 'dddword': 14\
        }

        self.w3grams_tid_vocab = {
            'This is a' : 1, 'unit test for' : 2, 'html2tfd.charngrams.BaseString2TF class for' : 3,\
            'is a unit' : 4, 'test for html2tfd.charngrams.BaseString2TF' : 5, 'class for html2vectors' : 6,\
            'a unit test' : 7, 'for html2tfd.charngrams.BaseString2TF class' : 8, 'for html2vectors package/module' : 9\
        }
        
        self.w3grams_tid_vocab_small = { 
            'This is a' : 1, 'unit test for' : 2, 'html2tfd.charngrams.BaseString2TF class for' : 3,\
            'is a unit' : 4, 'test for html2tfd.charngrams.BaseString2TF' : 5\
        }

        self.w3grams_tid_vocab_large = { 
          'This is a' : 1, 'unit test for' : 2, 'html2tfd.charngrams.BaseString2TF class for' : 3,\
            'is a unit' : 4, 'test for html2tfd.charngrams.BaseString2TF' : 5, 'class for html2vectors' : 6,\
            'a unit test' : 7, 'for html2tfd.charngrams.BaseString2TF class' : 8, 'for html2vectors package/module' : 9,\
          'aa bb cc' : 10, 'ee ff gg' : 11, 'hh ii jj' : 12\
        }

        #Terms-Frequencies (python) Dictionaries
        self.expected_c3grams_tf_dict = {
            's i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
            '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
            'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
            ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
            'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
            'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
            'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
            'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
            'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
            'vec': 1, ' fo': 2, 'a u': 1
        }

        self.expected_c3grams_tf_dict_smallVocab = {
            '2TF': 1, 'ase': 1, 'htm': 2, '/mo': 1, 'TF ': 1, '.ch': 1, ' un': 1, '2tf': 1, 'l2t': 1,\
            'l2v': 1, 'eSt': 1, 'ing': 1, 'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'Str': 1,\
            'for': 2, ' is': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
            'gra': 1, 'har': 1, 'is ': 2, 'F c': 1, 'ass': 1, 'g2T': 1, 'his': 1, 'kag': 1, 'Bas': 1,\
            '2ve': 1, 'ors': 1, 'it ': 1, 'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'Thi': 1, 'dul': 1,\
            ' te': 1, '.Ba': 1, 'nit': 1, 'las': 1, ' a ': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'ack': 1,\
            'age': 1, ' ht': 2, 'ms.': 1, 'ng2': 1, 'cto': 1, ' fo': 2, 'a u': 1
        }
        
        self.expected_words_tf_dict = {
            'a': 1, 'for': 2, 'This': 1, 'is': 1, 'html2vectors': 1, 'test': 1,\
            'package/module': 1, 'html2tfd.charngrams.BaseString2TF': 1, 'class': 1, 'unit': 1
        }

        self.expected_words_tf_dict_smallVocab = {
            'a': 1, 'for': 2, 'This': 1, 'is': 1, 'html2vectors': 1, 'test': 1,\
            'package/module': 1\
        }

        self.expected_w3grams_tf_dict = {
            'This is a' : 1, 'unit test for' : 1, 'html2tfd.charngrams.BaseString2TF class for' : 1,\
            'is a unit' : 1, 'test for html2tfd.charngrams.BaseString2TF' : 1, 'class for html2vectors' : 1,\
            'a unit test' : 1, 'for html2tfd.charngrams.BaseString2TF class' : 1, 'for html2vectors package/module' : 1\
        }

        self.expected_w3grams_tf_dict_smallVocab = {
            'This is a' : 1, 'unit test for' : 1, 'html2tfd.charngrams.BaseString2TF class for' : 1,\
            'is a unit' : 1, 'test for html2tfd.charngrams.BaseString2TF' : 1\
        }
        
        #Terms-Frequencies numpy.arrays
        self.expected_c3grams_tf_arr = np.array( [
            (' a ', 1.0), (' cl', 1.0), (' fo', 2.0), (' ht', 2.0), (' is', 1.0),\
            (' pa', 1.0), (' te', 1.0), (' un', 1.0), ('.Ba', 1.0), ('.ch', 1.0),\
            ('/mo', 1.0), ('2TF', 1.0), ('2tf', 1.0), ('2ve', 1.0), ('Bas', 1.0),\
            ('F c', 1.0), ('Str', 1.0), ('TF ', 1.0), ('Thi', 1.0), ('a u', 1.0),\
            ('ack', 1.0), ('age', 1.0), ('ams', 1.0), ('arn', 1.0), ('ase', 1.0),\
            ('ass', 1.0), ('cha', 1.0), ('cka', 1.0), ('cla', 1.0), ('cto', 1.0),\
            ('d.c', 1.0), ('dul', 1.0), ('e/m', 1.0), ('eSt', 1.0), ('ect', 1.0),\
            ('est', 1.0), ('fd.', 1.0), ('for', 2.0), ('g2T', 1.0), ('ge/', 1.0),\
            ('gra', 1.0), ('har', 1.0), ('his', 1.0), ('htm', 2.0), ('ing', 1.0),\
            ('is ', 2.0), ('it ', 1.0), ('kag', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
            ('las', 1.0), ('ml2', 2.0), ('mod', 1.0), ('ms.', 1.0), ('ng2', 1.0),\
            ('ngr', 1.0), ('nit', 1.0), ('odu', 1.0), ('or ', 2.0), ('ors', 1.0),\
            ('pac', 1.0), ('r h', 2.0), ('ram', 1.0), ('rin', 1.0), ('rng', 1.0),\
            ('rs ', 1.0), ('s a', 1.0), ('s f', 1.0), ('s i', 1.0), ('s p', 1.0),\
            ('s.B', 1.0), ('seS', 1.0), ('ss ', 1.0), ('st ', 1.0), ('t f', 1.0),\
            ('t t', 1.0), ('tes', 1.0), ('tfd', 1.0), ('tml', 2.0), ('tor', 1.0),\
            ('tri', 1.0), ('ule', 1.0), ('uni', 1), ('vec', 1)\
            ],\
            dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )
        
        self.expected_c3grams_tf_arr_Vocab = np.array( [
            ('s i', 1.0), ('t t', 1.0), ('ase', 1.0), ('s a', 1.0), ('htm', 2.0),\
            ('ram', 1.0), ('rs ', 1.0), ('TF ', 1.0), ('s f', 1.0), ('.ch', 1.0),\
            ('t f', 1.0), (' un', 1.0), ('2tf', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
            ('s p', 1.0), ('eSt', 1.0), ('tes', 1.0), ('ge/', 1.0), ('ams', 1.0),\
            ('or ', 2.0), ('cha', 1.0), ('est', 1.0), ('st ', 1.0), ('Str', 1.0),\
            ('for', 2.0), ('tor', 1.0), (' is', 1.0), ('ing', 1.0), ('cla', 1.0),\
            ('e/m', 1.0), ('fd.', 1.0), ('ml2', 2.0), ('pac', 1.0), ('arn', 1.0),\
            ('ngr', 1.0), ('r h', 2.0), ('2TF', 1.0), ('har', 1.0), ('is ', 2.0),\
            ('tml', 2.0), ('F c', 1.0), ('ass', 1.0), ('tri', 1.0), ('g2T', 1.0),\
            ('his', 1.0), ('kag', 1.0), ('Bas', 1.0), ('2ve', 1.0), ('tfd', 1.0),\
            ('gra', 1.0), ('rng', 1.0), ('ors', 1.0), ('it ', 1.0), ('odu', 1.0),\
            ('mod', 1.0), (' pa', 1.0), ('ect', 1.0), ('ule', 1.0), ('Thi', 1.0),\
            ('s.B', 1.0), (' te', 1.0), ('.Ba', 1.0), ('nit', 1.0), ('las', 1.0),\
            (' a ', 1.0), ('rin', 1.0), ('seS', 1.0), ('cka', 1.0), (' cl', 1.0),\
            ('d.c', 1.0), ('dul', 1.0), ('ack', 1.0), ('age', 1.0), (' ht', 2.0),\
            ('ms.', 1.0), ('/mo', 1.0), ('ng2', 1.0), ('ss ', 1.0), ('uni', 1.0),\
            ('cto', 1.0), ('vec', 1.0), (' fo', 2.0), ('a u', 1.0)\
            ],\
            dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
          )
            
            
        self.expected_c3grams_tf_arr_smallVocab = np.array( [
            ('2TF', 1.0), ('ase', 1.0), ('htm', 2.0), ('/mo', 1.0), ('TF ', 1.0),\
            ('.ch', 1.0), (' un', 1.0), ('2tf', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
            ('eSt', 1.0), ('ing', 1.0), ('ge/', 1.0), ('ams', 1.0), ('or ', 2.0),\
            ('cha', 1.0), ('est', 1.0), ('Str', 1.0), ('for', 2.0), (' is', 1.0),\
            ('cla', 1.0), ('e/m', 1.0), ('fd.', 1.0), ('ml2', 2.0), ('pac', 1.0),\
            ('arn', 1.0), ('ngr', 1.0), ('gra', 1.0), ('har', 1.0), ('is ', 2.0),\
            ('F c', 1.0), ('ass', 1.0), ('g2T', 1.0), ('his', 1.0), ('kag', 1.0),\
            ('Bas', 1.0), ('2ve', 1.0), ('ors', 1.0), ('it ', 1.0), ('odu', 1.0),\
            ('mod', 1.0), (' pa', 1.0), ('ect', 1.0), ('Thi', 1.0), ('dul', 1.0),\
            (' te', 1.0), ('.Ba', 1.0), ('nit', 1.0), ('las', 1.0), (' a ', 1.0),\
            ('cka', 1.0), (' cl', 1.0), ('d.c', 1.0), ('ack', 1.0), ('age', 1.0),\
            (' ht', 2.0), ('ms.', 1.0), ('ng2', 1.0), ('cto', 1.0), (' fo', 2.0),\
            ('a u', 1.0)\
            ],\
            dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )

        self.expected_words_tf_arr = np.array( [
            ('This', 1.0), ('a', 1.0), ('class', 1.0), ('for', 2.0),\
            ('html2tfd.charngrams.BaseString2TF', 1.0), ('html2vectors', 1.0),\
            ('is', 1.0), ('package/module', 1.0), ('test', 1.0), ('unit', 1.0)\
            ],\
            dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )                                          
        
        self.expected_words_tf_arr_Vocab = np.array( [
          ('a', 1.0), ('for', 2.0), ('This', 1.0), ('is', 1.0), ('html2vectors', 1.0),\
          ('test', 1.0), ('package/module', 1.0), ('html2tfd.charngrams.BaseString2TF', 1.0),\
          ('class', 1.0), ('unit', 1.0)\
          ],\
          dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )

        self.expected_words_tf_arr_smallVocab = np.array( [
          ('a', 1.0), ('for', 2.0), ('This', 1.0), ('is', 1.0), ('html2vectors', 1.0),\
          ('test', 1.0), ('package/module', 1.0)\
          ],\
          dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )

        self.expected_w3grams_tf_arr = np.array( [
          ('This is a', 1.0), ('a unit test', 1.0), ('class for html2vectors', 1.0),\
          ('for html2tfd.charngrams.BaseString2TF class', 1.0), ('for html2vectors package/module', 1.0),\
          ('html2tfd.charngrams.BaseString2TF class for', 1.0), ('is a unit', 1.0),\
          ('test for html2tfd.charngrams.BaseString2TF', 1.0), ('unit test for', 1.0)\
          ],\
          dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )

        self.expected_w3grams_tf_arr_Vocab = np.array( [
          ('a unit test', 1.0), ('html2tfd.charngrams.BaseString2TF class for', 1.0),\
          ('test for html2tfd.charngrams.BaseString2TF', 1.0), ('class for html2vectors', 1.0),\
          ('for html2tfd.charngrams.BaseString2TF class', 1.0), ('is a unit', 1.0),\
          ('for html2vectors package/module', 1.0), ('This is a', 1.0), ('unit test for', 1.0)\
          ],\
          dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )

        self.expected_w3grams_tf_arr_smallVocab = np.array( [
          ('is a unit', 1.0), ('test for html2tfd.charngrams.BaseString2TF', 1.0), ('unit test for', 1.0),\
          ('This is a', 1.0), ('html2tfd.charngrams.BaseString2TF class for', 1.0)\
          ],\
          dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')])\
        )

        #Frequencies scipy.sparse matrices 
        self.expected_c3grams_f_sparse_NoVocab = ssp.csr_matrix( 
          ([
            1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0\
           ],\
            (np.zeros(84), np.arange(84))
          ),\
            dtype=np.float32\
        )

        self.expected_c3grams_f_sparse_largeVocab = ssp.csr_matrix( 
          ([
            1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0\
           ],\
            (np.zeros(96), np.arange(96))
          ),\
            dtype=np.float32\
        )

        self.expected_c3grams_f_sparse_smallVocab = ssp.csr_matrix( 
          ([
            1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            1.0,\
           ],\
            (np.zeros(61), np.arange(61))
          ),\
            dtype=np.float32\
        )
 
        self.expected_words_f_sparse_Vocab = ssp.csr_matrix( 
          ([ 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            (np.zeros(11), np.arange(11))\
          ), dtype=np.float32\
        )

        self.expected_words_f_sparse_smallVocab = ssp.csr_matrix( 
          ([ 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            (np.zeros(8), np.arange(8))\
          ), dtype=np.float32\
        )

        self.expected_words_f_sparse_largeVocab = ssp.csr_matrix( 
          ([ 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0 ],\
            (np.zeros(15), np.arange(15))\
          ), dtype=np.float32\
        )

        self.expected_w3grams_f_sparse_Vocab = ssp.csr_matrix( 
          ([ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            (np.zeros(10), np.arange(10))\
          ), dtype=np.float32\
        )

        self.expected_w3grams_f_sparse_smallVocab = ssp.csr_matrix( 
          ([ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            (np.zeros(6), np.arange(6))\
          ), dtype=np.float32\
        )

        self.expected_w3grams_f_sparse_largeVocab = ssp.csr_matrix( 
          ([ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0 ],\
            (np.zeros(13), np.arange(13))\
          ), dtype=np.float32\
        )

        #Frequencies numpy.arrays matrices
        self.expected_c3grams_f_narray_Vocab = np.array( 
          ([
            1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0\
           ]),\
          dtype=np.float32\
        )

        self.expected_c3grams_f_narray_largeVocab = np.array( 
          ([
            1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0\
           ]),\
          dtype=np.float32\
        )

        self.expected_c3grams_f_narray_smallVocab = np.array( 
          ([
            1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,\
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0,\
            1.0,\
           ]),\
          dtype=np.float32\
        )

        self.expected_words_f_narray_Vocab = np.array( 
          [ 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            dtype=np.float32\
        )

        self.expected_words_f_narray_smallVocab = np.array( 
          [ 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            dtype=np.float32\
        )

        self.expected_words_f_narray_largeVocab = np.array( 
          [ 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0 ],\
            dtype=np.float32\
        )

        self.expected_w3grams_f_narray_Vocab = np.array( 
          [ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            dtype=np.float32\
        )

        self.expected_w3grams_f_narray_smallVocab = np.array( 
          [ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0 ],\
            dtype=np.float32\
        )

        self.expected_w3grams_f_narray_largeVocab = np.array( 
          [ 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0 ],\
            dtype=np.float32\
        )
                            

    """trms2tf_dict()"""
    def test_trms2tf_dict_c3grams_NoVocab(self):
        
        cngrams_tf_dict = trms2tfspd_dict( self.s2ngl_c3grams.terms_lst( self.txt_sample ), vocabulary=None )
        print cngrams_tf_dict
        self.assertEqual(cngrams_tf_dict, self.expected_c3grams_tf_dict) 

"""
    def test_trms2tf_dict_c3grams_Vocab(self):
        
        cngrams_tf_dict = trms2tf_dict( self.s2ngl_c3grams.terms_lst( self.txt_sample ), vocabulary=self.c3grams_tid_vocab )
        
        self.assertEqual(cngrams_tf_dict, self.expected_c3grams_tf_dict) 


    def test_trms2tf_dict_c3grams_smallVocab(self):
        
        cngrams_tf_dict = trms2tf_dict( self.s2ngl_c3grams.terms_lst( self.txt_sample ), vocabulary=self.c3grams_tid_vocab_small )
        
        self.assertEqual(cngrams_tf_dict, self.expected_c3grams_tf_dict_smallVocab)


    def test_trms2tf_dict_c3grams_largeVocab(self):
        
        cngrams_tf_dict = trms2tf_dict( self.s2ngl_c3grams.terms_lst( self.txt_sample ), vocabulary=self.c3grams_tid_vocab_large )
        
        self.assertEqual(cngrams_tf_dict, self.expected_c3grams_tf_dict)


    def test_trms2tf_dict_words_NoVocab(self):
        
        words_tf_dict = trms2tf_dict( self.s2ngl_words.terms_lst( self.txt_sample ), vocabulary=None )
        
        #Output excpected to be the same as in case of an input Vocabulary having same size (in terms) to the input terms-list.
        self.assertEqual(words_tf_dict, self.expected_words_tf_dict)  


    def test_trms2tf_dict_words_Vocab(self):
        
        cngrams_tf_dict = trms2tf_dict( self.s2ngl_words.terms_lst( self.txt_sample ), vocabulary=self.words_tid_vocab )
        
        self.assertEqual(cngrams_tf_dict, self.expected_words_tf_dict)   

    
    def test_trms2tf_dict_words_smallVocab(self):
        
        words_tf_dict = trms2tf_dict( self.s2ngl_words.terms_lst( self.txt_sample ), vocabulary=self.words_tid_vocab_small )
        
        #Output excpected to be the smaller that the _Vocabe case since input Vocabulary has smaller size (in terms) than terms-list.
        self.assertEqual(words_tf_dict, self.expected_words_tf_dict_smallVocab)    


    def test_trms2tf_dict_words_largeVocab(self):
        
        words_tf_dict = trms2tf_dict( self.s2ngl_words.terms_lst( self.txt_sample ), vocabulary=self.words_tid_vocab_large )
        
        #Output excpected to be the same as in case of an input Vocabulary having same size (in terms) to the input terms-list.
        self.assertEqual(words_tf_dict, self.expected_words_tf_dict)    


    def test_trms2tf_dict_w3grams_NoVocab(self):
        
        wngrams_tf_dict = trms2tf_dict( self.s2ngl_w3grams.terms_lst( self.txt_sample ), vocabulary=None )

        #Output excpected to be the same as in case of an input Vocabulary having same size (in terms) to the input terms-list.
        #Because, the input Vocabulary happess to have the same terms-order to the one returned by default in the case of 'Vocabulary = None'
        self.assertEqual(wngrams_tf_dict, self.expected_w3grams_tf_dict)


    def test_trms2tf_dict_w3grams_Vocab(self):
        
        wngrams_tf_dict = trms2tf_dict( self.s2ngl_w3grams.terms_lst( self.txt_sample ), vocabulary=self.w3grams_tid_vocab )
        
        self.assertEqual(wngrams_tf_dict, self.expected_w3grams_tf_dict)


    def test_trms2tf_dict_w3grams_smallVocab(self):
        
        wngrams_tf_dict = trms2tf_dict( self.s2ngl_w3grams.terms_lst( self.txt_sample ), vocabulary=self.w3grams_tid_vocab_small )
        
        self.assertEqual(wngrams_tf_dict, self.expected_w3grams_tf_dict_smallVocab)


    def test_trms2tf_dict_w3grams_largeVocab(self):
        
        wngrams_tf_dict = trms2tf_dict( self.s2ngl_w3grams.terms_lst( self.txt_sample ), vocabulary=self.w3grams_tid_vocab_large )
        
        #Output excpected to be the same as in case of an input Vocabulary having same size (in terms) to the input terms-list.
        self.assertEqual(wngrams_tf_dict, self.expected_w3grams_tf_dict)


    #trms2tf_narray()
    def test_trms2tf_narray_c3grams_NoVocab(self):
        
        cngrams_tf_arr = trms2tf_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
          vocabulary=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  

        self.assertTrue( np.all(cngrams_tf_arr == self.expected_c3grams_tf_arr) )


    def test_trms2tf_narray_c3grams_Vocab(self):
        
        cngrams_tf_arr = trms2tf_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            vocabulary=self.c3grams_tid_vocab,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        #Output excpected to be the same as in case of an input Vocabulary is None.
        #However, the order of terms will follow the one of input Vocabulary.
        self.assertTrue( np.all(cngrams_tf_arr == self.expected_c3grams_tf_arr_Vocab) )


    def test_trms2tf_narray_c3grams_smallVocab(self):

        cngrams_tf_arr = trms2tf_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            vocabulary=self.c3grams_tid_vocab_small,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
       
        #Output excpected to be smaller than input terms Vocabulary having same size (in terms) to the input terms-list.
        self.assertTrue( np.all(cngrams_tf_arr == self.expected_c3grams_tf_arr_smallVocab) )


    def test_trms2tf_narray_c3grams_largeVocab(self):
        
        cngrams_tf_arr = trms2tf_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            vocabulary=self.c3grams_tid_vocab_large,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        #Output excpected to be the same as in case a Vocabulary is given, having the same terms as the ones into the terms-list.
        #That is, the extra terms into the vocabulary will not be included into the output recored-array.
        self.assertTrue( np.all(cngrams_tf_arr == self.expected_c3grams_tf_arr_Vocab) )


    def test_trms2tf_narray_words_NoVocab(self):
        
        words_tf_arr = trms2tf_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        self.assertTrue( np.all(words_tf_arr == self.expected_words_tf_arr) )


    def test_trms2tf_narray_words_Vocab(self):
        
        words_tf_arr = trms2tf_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            vocabulary=self.words_tid_vocab,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        self.assertTrue( np.all(words_tf_arr == self.expected_words_tf_arr_Vocab) )


    def test_trms2tf_narray_words_smallVocab(self):
        
        words_tf_arr = trms2tf_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            vocabulary=self.words_tid_vocab_small,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        self.assertTrue( np.all(words_tf_arr == self.expected_words_tf_arr_smallVocab) )


    def test_trms2tf_narray_words_largeVocab(self):
        
        words_tf_arr = trms2tf_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            vocabulary=self.words_tid_vocab_large,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        #Output excpected to be the same as in case a Vocabulary is given, having the same terms as the ones into the terms-list.
        #That is, the extra terms into the vocabulary will not be included into the output recored-array.
        self.assertTrue( np.all(words_tf_arr == self.expected_words_tf_arr_Vocab) )


    def test_trms2tf_narray_w3grams_NoVocab(self):
        
        w3grams_tf_arr = trms2tf_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        self.assertTrue( np.all(w3grams_tf_arr == self.expected_w3grams_tf_arr) )


    def test_trms2tf_narray_w3grams_Vocab(self):
        
        w3grams_tf_arr = trms2tf_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            vocabulary=self.w3grams_tid_vocab,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        self.assertTrue( np.all(w3grams_tf_arr == self.expected_w3grams_tf_arr_Vocab) )


    def test_trms2tf_narray_w3grams_smallVocab(self):
        
        w3grams_tf_arr = trms2tf_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            vocabulary=self.w3grams_tid_vocab_small,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        self.assertTrue( np.all(w3grams_tf_arr == self.expected_w3grams_tf_arr_smallVocab) )


    def test_trms2tf_narray_words_largeVocab(self):
        
        words_tf_arr = trms2tf_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            vocabulary=self.words_tid_vocab_large,\
            norm_func=None, ndtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))  
        
        #Output excpected to be the same as in case a Vocabulary is given, having the same terms as the ones into the terms-list.
        #That is, the extra terms into the vocabulary will not be included into the output recored-array.
        self.assertTrue( np.all(words_tf_arr == self.expected_words_tf_arr_Vocab) )


    #trms2f_sparse()
    def test_trms2f_sparse_c3grams_NoVocab(self):
        
        with self.assertRaises(ValueError):
          cngrams_f_sparse = trms2f_sparse( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
              tid_vocabulary=None, norm_func=None, ndtype=np.float32 )


    def test_trms2f_sparse_c3grams_Vocab(self):
        
        cngrams_f_sparse = trms2f_sparse( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.c3grams_tid_vocab, norm_func=None, ndtype=np.float32 )
      
        self.assertTrue( np.all(cngrams_f_sparse.toarray() == self.expected_c3grams_f_sparse_NoVocab.toarray()) )


    def test_trms2f_sparse_c3grams_smallVocab(self):
        
        cngrams_f_sparse = trms2f_sparse( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.c3grams_tid_vocab_small, norm_func=None, ndtype=np.float32 )
        
        #Output excpected to be smaller in size than the input terms-list but same in size to the input Vocabulary.
        self.assertTrue( np.all(cngrams_f_sparse.toarray() == self.expected_c3grams_f_sparse_smallVocab.toarray()) )


    def test_trms2f_sparse_c3grams_largeVocab(self):
        
        cngrams_f_sparse = trms2f_sparse( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.c3grams_tid_vocab_large, norm_func=None, ndtype=np.float32 )
        
        #Output excpected to be larger in size than the input terms-list but same in size to the input Vocabulary.
        #terms-poisition of terms not inlcuded in terms-list being setted to zero.
        self.assertTrue( np.all(cngrams_f_sparse.toarray() == self.expected_c3grams_f_sparse_largeVocab.toarray()) )

    def test_trms2f_sparse_words_NoVocab(self):
        
        with self.assertRaises(ValueError):
          words_f_sparse = trms2f_sparse( self.s2ngl_words.terms_lst( self.txt_sample ),\
              tid_vocabulary=None, norm_func=None, ndtype=np.float32 )


    def test_trms2f_sparse_words_Vocab(self):
        
        words_f_sparse = trms2f_sparse( self.s2ngl_words.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.words_tid_vocab, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(words_f_sparse.toarray() == self.expected_words_f_sparse_Vocab.toarray()) )


    def test_trms2f_sparse_words_smallVocab(self):
        
        words_f_sparse = trms2f_sparse( self.s2ngl_words.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.words_tid_vocab_small, norm_func=None, ndtype=np.float32 )
        
        #Output excpected to be smaller in size than the input terms-list but same in size to the input Vocabulary.
        self.assertTrue( np.all(words_f_sparse.toarray() == self.expected_words_f_sparse_smallVocab.toarray()) )


    def test_trms2f_sparse_words_largeVocab(self):
        
        words_f_sparse = trms2f_sparse( self.s2ngl_words.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.words_tid_vocab_large, norm_func=None, ndtype=np.float32 )
        
        #Output excpected to be larger in size than the input terms-list but same in size to the input Vocabulary.
        #terms-poisition of terms not inlcuded in terms-list being setted to zero.
        self.assertTrue( np.all(words_f_sparse.toarray() == self.expected_words_f_sparse_largeVocab.toarray()) )


    def test_trms2f_sparse_w3grams_NoVocab(self):
        
        with self.assertRaises(ValueError):
          w3grams_f_sparse = trms2f_sparse( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
              tid_vocabulary=None, norm_func=None, ndtype=np.float32 )


    def test_trms2f_sparse_w3grams_Vocab(self):
        
        w3grams_f_sparse = trms2f_sparse( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.w3grams_tid_vocab, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(w3grams_f_sparse.toarray() == self.expected_w3grams_f_sparse_Vocab.toarray()) )


    def test_trms2f_sparse_w3grams_smallVocab(self):
        
        w3grams_f_sparse = trms2f_sparse( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.w3grams_tid_vocab_small, norm_func=None, ndtype=np.float32 )
        
        #Output excpected to be smaller in size than the input terms-list but same in size to the input Vocabulary.
        self.assertTrue( np.all(w3grams_f_sparse.toarray() == self.expected_w3grams_f_sparse_smallVocab.toarray()) )


    def test_trms2f_sparse_w3grams_largeVocab(self):
        
        w3grams_f_sparse = trms2f_sparse( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.w3grams_tid_vocab_large, norm_func=None, ndtype=np.float32 )
        
        #Output excpected to be larger in size than the input terms-list but same in size to the input Vocabulary.
        #terms-poisition of terms not inlcuded in terms-list being setted to zero.
        self.assertTrue( np.all(w3grams_f_sparse.toarray() == self.expected_w3grams_f_sparse_largeVocab.toarray()) )


    #trms2f_narray"
    def test_trms2f_narray_c3grams_NoVocab(self):
        
        with self.assertRaises(ValueError):
          cngrams_f_narray = trms2f_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
              tid_vocabulary=None, norm_func=None, ndtype=np.float32 )


    def test_trms2f_narray_c3grams_Vocab(self):
        
        cngrams_f_narray = trms2f_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.c3grams_tid_vocab, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(cngrams_f_narray == self.expected_c3grams_f_narray_Vocab) )


    def test_trms2f_narray_c3grams_smallVocab(self):
        
        cngrams_f_narray = trms2f_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.c3grams_tid_vocab_small, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(cngrams_f_narray == self.expected_c3grams_f_narray_smallVocab) )


    def test_trms2f_narray_c3grams_largeVocab(self):
        
        cngrams_f_narray = trms2f_narray( self.s2ngl_c3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.c3grams_tid_vocab_large, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(cngrams_f_narray == self.expected_c3grams_f_narray_largeVocab) )


    def test_trms2f_narray_words_NoVocab(self):
        
        with self.assertRaises(ValueError):
          words_f_narray = trms2f_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
              tid_vocabulary=None, norm_func=None, ndtype=np.float32 )


    def test_trms2f_narray_words_Vocab(self):
        
        words_f_narray = trms2f_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.words_tid_vocab, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(words_f_narray == self.expected_words_f_narray_Vocab) )


    def test_trms2f_narray_words_smallVocab(self):
        
        words_f_narray = trms2f_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.words_tid_vocab_small, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(words_f_narray == self.expected_words_f_narray_smallVocab) )


    def test_trms2f_narray_words_largeVocab(self):
        
        words_f_narray = trms2f_narray( self.s2ngl_words.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.words_tid_vocab_large, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(words_f_narray == self.expected_words_f_narray_largeVocab) )


    def test_trms2f_narray_w3grams_NoVocab(self):
        
        with self.assertRaises(ValueError):
          w3grams_f_narray = trms2f_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
              tid_vocabulary=None, norm_func=None, ndtype=np.float32 )


    def test_trms2f_narray_w3grams_Vocab(self):
        
        w3grams_f_narray = trms2f_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.w3grams_tid_vocab, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(w3grams_f_narray == self.expected_w3grams_f_narray_Vocab) )


    def test_trms2f_narray_w3grams_smallVocab(self):
        
        w3grams_f_narray = trms2f_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.w3grams_tid_vocab_small, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(w3grams_f_narray == self.expected_w3grams_f_narray_smallVocab) )


    def test_trms2f_narray_w3grams_largeVocab(self):
        
        w3grams_f_narray = trms2f_narray( self.s2ngl_w3grams.terms_lst( self.txt_sample ),\
            tid_vocabulary=self.w3grams_tid_vocab_large, norm_func=None, ndtype=np.float32 )
        
        self.assertTrue( np.all(w3grams_f_narray == self.expected_w3grams_f_narray_largeVocab) )

"""
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TF) )
unittest.TextTestRunner(verbosity=2).run(suite)        
