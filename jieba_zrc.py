import getZrc
from sklearn.feature_extraction.text import TfidfTransformer
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
zrc=getZrc.getZrc("files/hanyu1.zrc")
zrc_list = jieba.cut_for_search(zrc) 
print("Search Mode: " + "/".join(zrc_list))
print(zrc_list)
tfidf = transformer.fit_transform(vectorizer.fit_transform(zrc_list))
word = vectorizer.get_feature_names()
weight = tfidf.toarray()
#print(weight)	
#print(word)	
