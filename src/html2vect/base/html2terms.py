#
#    Module: html2terms
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.html2terms: submodule of `html2vect` module defines the classes: BaseHtml2TF"""

import abc
import warnings
from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.io.basefilehandlers import BaseFileHandler
from ..tools import tfdtools 


class BaseHtml2TF(BaseFileHandler):
    __metaclass__ = abc.ABCMeta

 
    def __init__(self, attrib, lowercase, valid_html):
        
        #Initialise BaseFileHandler Class
        super(BaseHtml2TF, self).__init__()   
        
        #HTML to attributes Class
        self.h2attr = BaseHTML2Attributes( valid_html )
        
        #Initialised the TermsType to be produced from this class stored in as class attribute 
        self.__class__.s2ngl.reset_N(n)
        
        #String to Term Frequency Class using  
        self.s2tf = BaseString2TF( self.__class__.s2ngl )    
        
        if attrib == "text":
            self.attrib__ = self.h2attr.text
        elif attrib == "tags":
            self.attrib__ = self.h2attr.tags
        else:
            raise Exception("Invalid attribute: only HTML 'text' or 'tags' can be retured for now")
                        
        if lowercase:
            self._attrib = self._lower( self.attrib__ )    
        else:
            self._attrib = self.attrib__
   
    
    def _lower(self, methd):
        
        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()
        
        return lowerCase
    
    
    def build_vocabulary(self,xhtml_file_l, encoding, error_handling):
         
        #The TF Dictionary 
        tf_d = dict()
        #Merge All Term-Frequency Dictionaries created by the Raw Texts
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            tf_d = tfdtools.merge_tfds( tf_d, self.s2tf.tf_dict( self._attrib( html_str ) ) )
            
        #Create The Terms-Index Vocabulary that is shorted by Frequency descending order
        #tid_vocabulary = tfdtools.tf2tidx( tf_d )

        tid_vocabulary = tf_d
        
        return tid_vocabulary
    
    
    def __build_vocabulary(self,*args, **kwrgs):
        
        #Warn me that a Vocabulary is automaticaly buildined  
        warnings.warn("Automated Vocabulary Building has been triggered: NONE tid_vocabulary has been given as argument")
        
        #Build and return the Vocabulary
        return self.build_vocabulary(*args, **kwrgs)
        
        
    @abc.abstractmethod        
    def yield_(self, xhtml_str, tid_vocabulary): 
        #The main method that will produce the Term-Frequency or Frequency Dictionaries/Lists
        pass
    
     
    @abc.abstractmethod    
    def from_src(self, xhtml_str, tid_vocabulary=None):
        pass


    @abc.abstractmethod    
    def from_files(self, xhtml_file_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):
        pass

    
    @abc.abstractmethod    
    def from_paths(self, basepath, filepath_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):
       pass
            

        
        

    