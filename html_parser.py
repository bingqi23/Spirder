# coding:utf8
from bs4 import BeautifulSoup
import re
import urlparse
import urllib

class HtmlParser(object):

	def _get_new_title(self,soup):
		title = soup.find('head').find('title')
		new_title = str(title)[7:-63]
		#print new_title
		return new_title

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r"/art/xiaoshuo/*"), target=re.compile(r"_blank"))
		#print links
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, soup):
		img_urls = set()
		content = soup.find_all("div",attrs={"class": "artbody imgbody"})
		#print content
		return content

	def parse(self, page_url, html_cont):
		if html_cont is None:
			return
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(soup)
		new_title = self._get_new_title(soup)
		return new_urls, new_data, new_title