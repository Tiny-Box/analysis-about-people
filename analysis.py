#encoding:utf-8
import os
import jieba.posseg as pseg


class person(object):
	"""docstring for person"""
	def __init__(self, arg):
		super(person, self).__init__()
		self.articlelist = os.listdir(arg)
		

fileaddress = "D:\\wya"
# fileaddress2 = "D:\\llr"
# fileaddress3 = "D:\\zjw"

flist = os.listdir(fileaddress)
# flist2 = os.listdir(fileaddress2)
# flist3 = os.listdir(fileaddress3)

dic = {}
sta = {}
flag = ['j', 'ad', 'p', 'zg', 'vn', 'an', 'eng', 'nz', 'mq', 'nr', 'ns', 'nt', 'v', 'a', 'c', 'b', 'd', 'f', 'i', 'k', 'uv', 'm', 'l', 'n', 'q', 'ul', 's', 'r', 'u', 't', 'uj', 'y', 'ud', 'ug', 'z']
flag_s = ['n','nt','nd','nl','nh','nhh','nhf','nhg','nhy','nhr','nhw','ns','nn','ni','nz','v','vu','vd','vl','aq','as','f','m','q','d','r','p','c','u','e','o','i','in','iv','ia','ic','j','jn','jv','ja','h','k','g','x','w','wp','ws','wu']
flag_f = ['j', 'ad', 'p', 'zg', 'vn', 'an', 'eng', 'nz', 'mq', 'nr', 'ns', 'nt', 'v', 'a', 'c', 'b', 'd', 'f', 'i', 'k', 'uv', 'm', 'l', 'n', 'q', 'ul', 's', 'r', 'u', 't', 'uj', 'y', 'ud', 'ug', 'z', 'x', 'nrt', 'o', 'uz', 'df', 'ng', 'vq', 'e', 'nrfg', 'rz', 'vi', 'h', 'vg', 'rr', 'ag', 'tg', 'vd', 'g', 'dg', 'yg', 'rg', 'mg']

for x in flag_f:
	dic[x] = []
	sta[x] = 0

for x in flist:
	with open(fileaddress + "\\" + x) as f:
		data = f.read()
		words = pseg.cut(data)
		for w in words:
			if w.flag != "x":
				dic[w.flag].append(w.word)
				sta[w.flag] += 1


for k in sta:
	print k + " is ", sta[k]



# for i in flist1:
# 	with open(fileaddress1 + "\\" + i) as f:
# 		data = f.read()
# 		words = pseg.cut(data)
# 		for w in words:
# 			if w.flag not in flag_f:
# 				flag_f.append(w.flag)
# 		print i + "is ok"

# for i in flist2:
# 	with open(fileaddress2 + "\\" + i) as f:
# 		data = f.read()
# 		words = pseg.cut(data)
# 		for w in words:
# 			if w.flag not in flag_f:
# 				flag_f.append(w.flag)
# 		print i + "is ok"

# for i in flist3:
# 	with open(fileaddress3 + "\\" + i) as f:
# 		data = f.read()
# 		words = pseg.cut(data)
# 		for w in words:
# 			if w.flag not in flag_f:
# 				flag_f.append(w.flag)
# 		print i + "is ok"


# print flag_f

# for w in words:
# 	if w.flag != "x":
# 		dic[w.flag].append(w.word)

# for i in dic["n"]:
# 	print i