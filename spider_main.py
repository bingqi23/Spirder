# coding:utf8
import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print 'craw %d : %s' % (count, new_url)
				html_cont = self.downloader.download(new_url)
				#print html_cont
				new_urls, new_data ,new_title= self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				#self.outputer.collect_data(new_data)
				#self.outputer.downloadImg(new_data, new_title)
				self.outputer.downloadTxt(new_data, new_title);
				if count == 100:
					break
				count = count + 1
			except:
				print 'craw failed'
				#break

		#self.outputer.output_html()

if __name__=="__main__":
	#root_url = "http://www.2277r.com/art/setu/katongdongman/"
	root_url = "http://www.2277r.com/art/xiaoshuo/dushijiqing/"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)