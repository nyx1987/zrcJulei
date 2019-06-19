# coding=UTF-8
import re
import sys
from imp import reload
reload(sys)
sys.setdefaultencoding('utf8')
#功能：是否包含汉字
def have_cn(str):
	return re.compile(u'[\u4e00-\u9fa5]').search(str)
def have_jp(str):#识别平假名和片假名
	return re.compile(u'[\u3040-\u309F]').search(str) or re.compile(u'[\u30A0-\u30FF]').search(str)
def have_ko(str):
	return re.compile(u'[\uAC00-\uD7A3]').search(str)
def getZrc(file):
	fo = open(file, "rw+")
#	pattern0 = re.compile(r'[\\[(.*?)\\]')
	pattern0 = re.compile(r'[<](.*?)[>]')
	pattern1 = re.compile(r'[\[](.*?)[\]]')
	pattern2 = re.compile(r'[<](.*?)[>]')
	ct=fo.read();
	ct0 = re.sub(pattern0,' ',ct)
	ct1 = re.sub(pattern1,' ',ct0)
	ct2 = re.sub(pattern2,' ',ct1)
	ct2 = ct2.replace(' ','')
	ct2=ct2.replace('\r\n','')
	ct2=ct2.replace('\n','')
	ct2=ct2.replace(':','')
	ct2=ct2.replace('：','')
	ct2=ct2.replace('作词','')
	ct2=ct2.replace('作曲','')
	#ct3 = ct2.replace("\n","")
	#print(ct3)
	fo.close()
	return ct2

#功能：检查是否是中文歌
def checkCH(ct):
	if (have_cn(ct)):
		if (have_jp(ct)):
			print ('日语歌曲，识别的字为: '+have_jp(ct).group(0).encode("utf8"))
			return False
		if (have_ko(ct)):
			print ('韩语歌曲，识别的字为: '+have_ko(ct).group(0).encode("utf8"))
			return False
		return True
	else:
		print ("其他语言歌曲")
		return False

def isZh(str):
	for ch in str.decode('utf-8'):
		if u'\u4e00' <= ch <= u'\u9fff':
#			print(333)
			i=[]
			#return True
		else:
			#print(ch)
			return False
	return True

#zrc=getZrc("files/hanyu1.zrc")
#zrc=getZrc("files/kor1.zrc")

#print(zrc)
#checkCH(zrc)
#isZh(zrc)
