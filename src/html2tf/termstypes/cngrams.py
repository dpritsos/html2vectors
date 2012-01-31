#
#    Module: cngrams - Character NGrams    
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2tf.termstypes.cngrams: submodule of `html2tf` module defines the class String2CNGramsList """ 



class String2CNGramsList(object):
    """ String2CNGramsList: Class
        Instance requires the size of NGrams. 
        Methods:
            - terms_lst(text): is getting a Text and returns a list of NGrams with size
                equal to the size defined while instantiation """
    
    def __init__(self, n):
        self.n = n
    
    def terms_lst(self, text):
        
        #In case not text is given it returns None. The outer code layer should handle this if caused due to error. 
        if not text:
            return None
        
        #Cut the text into tokens size defined in instantiation of this class and put them in a List 
        terms_l =  list()
        for i in range( len(text) - self.n + 1 ): 
            terms_l.append( text[i : i+self.n]  )
               
        return terms_l