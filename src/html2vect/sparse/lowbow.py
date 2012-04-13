#
#    Module: LowBOW (Local Weighted Bag of Words) - from html row text/files to scipy.sparse.csr_matrix LowBOW
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.sparse.lowbow: submodule of `html2vect` module defines the classes: Html2LBN(), Html2LBW()"""

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2lowbow import BaseString2LB
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.convert.tfdtools import TFDictTools
from io import IO

from ..base.termstypes.cngrams import String2CNGramsList
from ..base.termstypes.words import String2WordList

import scipy.sparse as ssp
import numpy as np
from scipy import stats
import string


class Html2LBN(BaseString2LB, BaseString2TF, TFDictTools, BaseHTML2Attributes, IO):
    
    def __init__(self, n, attrib, lowercase, valid_html, smoothing_kernel=stats.norm):
        IO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2LB.__init__(self, String2CNGramsList( n ), smoothing_kernel)
        BaseString2TF.__init__(self, String2CNGramsList( n ) )
        if attrib == "text":
            self._attrib_ = self.text
        elif attrib == "tags":
            self._attrib_ = self.tags            
        if lowercase:
            self._attrib_ = self._lower( self._attrib_ )
    
 
    def _attrib(self, xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling):  
        #Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            print "Creating Dictionary"
            tf_d = dict()
            #Merge All Term-Frequency Dictionaries created by the Raw Texts
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                tf_d = self.merge_tfds( tf_d, self.tf_dict( self._attrib_( html_str ) ) )
                
            #Create The Terms-Index Dictionary that is shorted by Frequency descending order
            tid_dictionary = self.tf2tidx( tf_d )
            
        print "Creating LowBOWs"
        #Create the LowBow Sparse Matrix for the whole corpus
        lowbow_lst = list()
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            lowbow_lst.append( self.lowbow( self._attrib_( html_str ), smth_pos_l, smth_sigma, tid_dictionary) )
        
        #Pack it as a sparse vstack and return it
        smth_copus_mtrx = ssp.vstack( lowbow_lst )
        return ( ssp.csr_matrix(smth_copus_mtrx, shape=smth_copus_mtrx.shape, dtype=np.float64), tid_dictionary ) 
    
    
    def _lower(self, methd):
        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()
        return lowerCase
        
        

class Html2LBW(Html2LBN):
    
    def __init__(self, attrib, lowercase, valid_html, smoothing_kernel=stats.norm):
        IO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2LB.__init__(self, String2WordList(), smoothing_kernel)
        BaseString2TF.__init__(self, String2WordList() )
        if attrib == "text":
            self._attrib_ = self.text
        elif attrib == "tags":
            self._attrib_ = self.tags            
        if lowercase:
            self._attrib_ = self._lower( self._attrib_ )
  
    