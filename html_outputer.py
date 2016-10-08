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
			#print "ok"
			pass
		else:
			os.mkdir(file_path)

		for data in data_urls:
			strings = data.split('/')
			local = strings[-1]
			file_name = str(file_path) + '/' + str(local)
			#print file_name
			urllib.urlretrieve(data, file_name)
		pass