# coding:utf8
import urllib2

class HtmlDownloader(object):

	def download(self, url):
		if url is None:
			print "url is None"
			return None

		request = urllib2.Request(url)
		request.add_header("user-agent","Mozilla/5.0")
		response = urllib2.urlopen(request)
		if response.getcode() != 200:
			print 'Error'+response.getcode()
			return None
		return response.read()