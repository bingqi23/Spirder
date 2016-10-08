# coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse
import urllib

class HtmlParser(object):

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r"/art/setu/*"))
		#print links
		for link in links:
			#print link
			new_url = link['href']
			#path1 = link['title']
			#print path1
			#print new_url
			new_full_url = urlparse.urljoin(page_url, new_url)
			#print new_full_url
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, soup):
		img_urls = set()
		src_urls = soup.find_all('img')
		for link in src_urls:
			src_url = link['src']
			img_urls.add(src_url)
			#print src_url
		return img_urls

	def parse(self, page_url, html_cont):
		if html_cont is None:
			return
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(soup)

		return new_urls, new_data