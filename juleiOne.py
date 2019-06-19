#encoding=utf-8
import getZrc0
import zrcWeight
import fileInfo_test
import jieba
import numpy as np
from pylab import *
from scipy import sparse
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
#zrc=getZrc.getZrc("files/hanyu1.zrc")
path= "/Users/wwwroot/python/zrcJulei/files/zrc5/"
files=fileInfo_test.getFilesName(path)
zrcAllWord=[]
ii=0
for filename in files:
	zrc=getZrc0.getZrc(path+filename+".zrc")
	#zrc=getZrc.getZrc("files/kor1.zrc")
	if zrc:
		if getZrc0.isZh(zrc):
			seg_list = jieba.cut_for_search(zrc)
			zrcStr= " ".join(seg_list)
			num=len(zrcStr)
			if zrcStr and num>50:
				weight,word=zrcWeight.getWeight(zrcStr)
				if word:
					ii+=1
#					print word
					zrcAllWord=zrcAllWord+word
			#else:
		#else:
			#print filename
#print zrc
		#zrcWeight.showWeight(weight,word)
#print(i)
zrcWord=list(set(zrcAllWord))
#print zrcAllWord
#print(len(zrcWord2))
#print(len(zrcWord))
dataArray = []
songid = []
jj=0
for filename in files:
	zrc=getZrc0.getZrc(path+filename+".zrc")
	#zrc=getZrc.getZrc("files/kor1.zrc")
	if zrc:
		if getZrc0.isZh(zrc):
			seg_list = jieba.cut_for_search(zrc)
			zrcStr= " ".join(seg_list)
			num=len(zrcStr)
			if zrcStr and num>50:
				weight,word=zrcWeight.getWeight(zrcStr)
				if word:
					songid.append(filename)
					for i in range(len(weight)):
						for j in range(len(word)):
							#print word[j],weight[i][j]
							dataArray.append([jj,zrcWord.index(word[j]),weight[i][j]])
							#dataArray.append([jj,word[j],weight[i][j]])
					jj +=1
#print zrcWord
#print(i)
#zrcWord=list(set(zrcAllWord))
#print(len(zrcWord2))
dataArray = np.array(dataArray).astype('float64')
row = dataArray[:, 0] #index
col = dataArray[:, 1] #userid
num = dataArray[:, 2] #num
#arr = sparse.coo_matrix((num, (row, col)), shape=((ii+1),len(zrcWord))).toarray()
arr = sparse.coo_matrix((num, (row, col)), shape=(len(songid),len(zrcWord))).toarray()
y_pred = KMeans(n_clusters=20).fit_predict(arr)
new_arr = PCA(n_components=5).fit_transform(arr)

plt.scatter(new_arr[:, 0], new_arr[:, 1], c=y_pred)
plt.show()
print(y_pred)
#print(songid)
res=[]
songidIndex=0
#print songidIndex
s3 = {}
result = []
for index, i in enumerate(y_pred):
	if s3.get(i):
 		s3[i].append(songid[index])
	else:
		s3[i] = [songid[index]]
for k, v in s3.items():
	result.append(v)
#print(result)
for t in result:
	print t
