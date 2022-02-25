"""
Web Scraping Example
@author Alvaro Ortega

"""

from urllib.request import urlopen
import bs4

from html_builder import HtmlBuilder

from article import Article


class Webpage(object):
    def __init__(self):
        pass

    @staticmethod
    def read(url):
        page = urlopen(url)
        return page.read()


class WebediaGroup(object):
    def __init__(self, url):
        self.__url = url

    def __parse_html(self, html):
        parse = bs4.BeautifulSoup(html, features='html.parser')
        articles = parse.find_all("article")
        articles_list = []
        for article in articles:
            try:
                image = article.a.picture.source.get('srcset')
                author = article.find("a", "abstract-author").getText()
                title_element = article.h2
                title = title_element.getText()
                url = title_element.a.get('href')
                resume = article.find("div", "abstract-excerpt").p.getText()
                time = article.time.getText()
                articles_list.append(Article(author, time, resume, title, url, image))
            except AttributeError:
                pass
        return articles_list

    def get_articles(self):
        html = Webpage.read(self.__url)
        articles = self.__parse_html(html)
        return articles


if __name__ == '__main__':
    xataka = WebediaGroup('https://www.xataka.com').get_articles()
    applesfera = WebediaGroup('https://www.applesfera.com').get_articles()
    html = HtmlBuilder()
    html.append_data(xataka, 'Xataka')
    html.append_data(applesfera, 'Applesfera')
    html.write_html()
