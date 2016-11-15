# -*- coding: utf-8 -*-
import urllib
import os

class HtmlOutputer(object):
	def __init__(self):
		self.datas=[]

	def collect_data(self, data):
		if data is None:
			return
		self.data.append(data)

	def output_html(self):
		pass

	def downloadImg(self, data_urls, data_title):
		file_path = "./pic/"+ data_title
		if os.path.exists(file_path):
			pass
		else:
			os.mkdir(file_path)

		for data in data_urls:
			strings = data.split('/')
			local = strings[-1]
			file_name = str(file_path) + '/' + str(local)
			urllib.urlretrieve(data, file_name)
		pass

	def downloadTxt(self, data_content, data_title):
		if os.path.exists("./TXT"):
			pass
		else:
			os.mkdir("./TXT")
		f=open("TXT/"+data_title+".txt",'w')
		f.write(str(data_content[0]))
		f.flush()
		f.close()
		pass