
""" """

import htmlattrib.regex

h2t = htmlattrib.regex.HtmlText() 
   
#genres = [ "blog/html/", "eshop/html/", "faq/html/", "frontpage/html/", "listing/html/", "php/html/", "spage/html/"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
genres = [ "blog_pgs/html_500/", "news_pgs/html_500/", "product_pgs/html_500/", "forum_pgs/html_500/", "wiki_pgs/html_500/" ] 
base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_3000/"
#genres = [ "html/" ] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
#text_path = "/txt_html2vectors_mod/"
text_path = "/txt_html2vectors_mod_500/"

for g in genres:
    fn_ftxt_l = h2t.from_paths(base_filepath, g, encoding='utf-8', error_handling='replace', low_mem=False)
    fn_ftxt_l = [ [fn.replace('/html_500/', text_path), ftxt] for fn, ftxt in fn_ftxt_l ]
    fn_ftxt_l = [ [fn.replace('.html', '.html.txt'), ftxt] for fn, ftxt in fn_ftxt_l ]
    h2t.save_files(None, fn_ftxt_l, encoding='utf-8', error_handling='strict')
   
