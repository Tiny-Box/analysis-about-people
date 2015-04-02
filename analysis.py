#encoding:utf-8
import os
import jieba.posseg as pseg


class person(object):
	"""docstring for person"""


	def __init__(self, arg):
		for x in flag_f:
			dic[x] = []
		self.articlelist = [ arg + "\\" + x for x in os.listdir(arg)]
		for i in self.articlelist:
			with open(i) as f:
				self.corpus.append(f.read())

fileaddress = "D:\\wya"

flist = os.listdir(fileaddress)

dic = {}
sta = {}
flag = ['j', 'ad', 'p', 'zg', 'vn', 'an', 'eng', 'nz', 'mq', 'nr', 'ns', 'nt', 'v', 'a', 'c', 'b', 'd', 'f', 'i', 'k', 'uv', 'm', 'l', 'n', 'q', 'ul', 's', 'r', 'u', 't', 'uj', 'y', 'ud', 'ug', 'z']
flag_s = ['n','nt','nd','nl','nh','nhh','nhf','nhg','nhy','nhr','nhw','ns','nn','ni','nz','v','vu','vd','vl','aq','as','f','m','q','d','r','p','c','u','e','o','i','in','iv','ia','ic','j','jn','jv','ja','h','k','g','x','w','wp','ws','wu']
flag_f = ['j', 'ad', 'p', 'zg', 'vn', 'an', 'eng', 'nz', 'mq', 'nr', 'ns', 'nt', 'v', 'a', 'c', 'b', 'd', 'f', 'i', 'k', 'uv', 'm', 'l', 'n', 'q', 'ul', 's', 'r', 'u', 't', 'uj', 'y', 'ud', 'ug', 'z', 'x', 'nrt', 'o', 'uz', 'df', 'ng', 'vq', 'e', 'nrfg', 'rz', 'vi', 'h', 'vg', 'rr', 'ag', 'tg', 'vd', 'g', 'dg', 'yg', 'rg', 'mg']

testone = person(fileaddress)

print testone.articlelist

# for x in flag_f:
# 	dic[x] = []
# 	sta[x] = 0

# for x in flist:
# 	with open(fileaddress + "\\" + x) as f:
# 		data = f.read()
# 		words = pseg.cut(data)
# 		for w in words:
# 			if w.flag != "x":
# 				dic[w.flag].append(w.word)
# 				sta[w.flag] += 1


# for k in sta:
# 	print k + " is ", sta[k]



