#encoding=utf-8
#encoding=utf-8
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
def getWeight(zrc):
	zrcList=[zrc]
	tfidf = transformer.fit_transform(vectorizer.fit_transform(zrcList))
	word = vectorizer.get_feature_names()
	weight = tfidf.toarray()
	return weight,word

def showWeight(weight,word):
	for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
		print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------")
		for j in range(len(word)):
			print(word[j],weight[i][j])


def getWord(weight,word):
	for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
		print(u"-------这里输出第",i,u"类文本的词语tf-idf权重------")
		for j in range(len(word)):
			print(word[j],weight[i][j])
#showWeight(weight)
