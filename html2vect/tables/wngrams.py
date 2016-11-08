#
#    Module: Words N-Grams - from html row text/files to PyTables EArrays Words N-Grams Earrays
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.tables.wngrams: submodule of `html2vect` module defines the classes: Html2TF() """

from .cngrams import Html2TF as CHtml2TF
from .cngrams import Html2TV as CHtml2TV
from ..base.termstypes.wngrams import String2WNGramsList


class Html2TF(CHtml2TF):

    # Define the TermsType to be produced from this class
    s2ngl = String2WNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initialise BaseHtml2TF Class
        super(Html2TF, self).__init__(*args, **kwrgs)


class Html2TV(CHtml2TV):

    # Define the TermsType to be produced from this class
    s2ngl = String2WNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initialise BaseHtml2TF Class
        super(Html2TV, self).__init__(*args, **kwrgs)


# To Be Written
class Html2TPL(object):

    def __init__(self):
        pass
