import os

def getfiles(path,suffix):
	list = []
	#path = "/Users/wwwroot/python/zrcJulei/files/zrc2"
	dirs = os.listdir(path)
#	print dirs
	for i in dirs:
		if os.path.splitext(i)[1] == suffix:
			list.append(i)
	return list
def getFilesName(path):
	list = []
	dirs = os.listdir(path)
	for i in dirs:
		if os.path.splitext(i)[1] == ".zrc":
			i=i.replace(".zrc","")
			list.append(i)
	return list

def getFilesFvName(path):
	list = []
	#path = "/Users/wwwroot/python/zrcJulei/files/zrc2"
	dirs = os.listdir(path)
	for i in dirs:
		if os.path.splitext(i)[1] == ".fv":
			#i=i.replace(".","")
			name=path+i
			list.append(name)
	return list
#list = getFilesName()
#print(list)
