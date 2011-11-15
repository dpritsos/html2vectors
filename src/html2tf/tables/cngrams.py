""" """

from htmlattrib.attrib import HtmlText
from html2tf.dictionaries.cngrams import BaseString2NgramList 
import tbtools
import numpy as np


class BaseString2TFTP(BaseString2NgramList):
    
    def __init__(self, n):
        self.n = n
        self.ngrms_l = list()
            
    def tf_array(self, text, ndtype=tbtools.default_TF_3grams_dtype):
        if not text:
            return None
        #Find and Count NGrams
        if not self.ngrms_l:
            self.terms_lst(text)
        terms, inds = np.unique1d(self.ngrms_l, return_inverse=True)
        freqs = np.bincount(inds)
        #We need a Recored arrays to be created thus using numpy.rec.array.fromarrays()
        #to be invoked as follows (alternatively fromarrays() can be used directly   
        NgF_arr = np.rec.array([terms, freqs], dtype=ndtype) 
        return NgF_arr
    
    def tpos_array(self, text, ndtype=tbtools.default_TP_3grams_dtype):
        if not text:
            return None
        #Find and Count NGrams
        if not self.ngrms_l:
            self.terms_lst(text)
        terms, inds = np.unique1d(self.ngrms_l, return_inverse=True)
        NgP_arr = np.rec.array(terms, dtype=ndtype)
        ###NEEDS OTHER SOLUTION NOT FOR USE YET!!!
        pos_arr_arr =[np.where(inds == idx) for idx in np.arange(len(terms))] 
        #return pos_arr_arr
        NgP_arr = np.rec.array([terms, pos_arr_arr], dtype=ndtype)
        return NgP_arr
    

class Html2TF(BaseString2TFTP, HtmlText):
    
    def __init__(self, n=3, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ).lower() )
    
    
class Html2TP(BaseString2TFTP, HtmlText):
    
    def __init__(self, n=3, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.npos_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.npos_dict( self.text( xhtml_str ).lower() )
    