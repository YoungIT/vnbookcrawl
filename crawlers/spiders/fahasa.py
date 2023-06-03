import re, unicodedata
from ..utils.requester import get_response
import pandas as pd
from bs4 import BeautifulSoup
from ..models.book import Book
import csv

from loguru import logger

logger.add("logging/fahasa.log", backtrace=True, diagnose=True)

class Fahasa:
   
    def __init__(self, base_url, genere, page_num, page_max):
        self.base_url = base_url.split("?")[0]
        self.genere = genere
        self.page_num = page_num
        self.page_max = page_max

    def getBooks(self):

        booklinks=[]
        page_num = self.page_num
        page_max = self.page_max
        
        while page_num<page_max:
            try:

                logger.info(f"Crawling Page {page_num} of {self.base_url}")

                page_url = f"{self.base_url}?order=num_orders&limit=24&p={page_num}"

                response = get_response(page_url)
                soup = BeautifulSoup(response.content, 'html.parser')

                book_div = soup.findAll("h2",{"class":"product-name-no-ellipsis p-name-list"})
                if len(book_div) == 0:
                    break
                else:
                    for link in book_div:
                        booklinks.append(link.a['href'])

                if page_num == page_max:
                    break 

                page_num += 1
            except:
                pass
        
        bookRead = []
        for book in booklinks:
            try:
                logger.debug(f"Reading book: {book}")
                br = self.readBooks(book)
                bookRead.append(br)
            except:
                pass

        return bookRead

    def readBooks(self, booklinks):
        response = get_response(booklinks)
        # parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        book_div = soup.find('div',{'class':'product_view_tab_content_ad'})
        table = book_div.find('table')

        df = pd.read_html(str(table))[0]
        # initate new instance of class book with empty arguments
        book = Book('', '', '', '', '', '', '', '', '')

        # extract the book title
        book_title = re.sub("(?m)^\s+","", soup.h1.text.rstrip())

        # extract the book price
        book_price = unicodedata.normalize("NFKD",soup.findAll("span",{"class":"price"})[-1].text)

        # extract book's author
        author_name = ''
        try:
            author_name = df[1][df.index[df[0].str.contains("Tác giả")].to_list()[0]]
        except:
            pass

        # extract translater
        translator = ''
        try:
            translator = df[1][df.index[df[0].str.contains("Người Dịch")].to_list()[0]]
        except:
            pass

        # extract publisher
        publisher = ''
        try:
            publisher = df[1][df.index[df[0].str.contains("NXB")].to_list()[0]]
        except:
            pass

        # extract book's total page
        num_pages = ''
        try:
            num_pages = df[1][df.index[df[0].str.contains("Số trang")].to_list()[0]]
        except:
            pass

        # get book description
        description_text = ''
        try:
            description_text = soup.find("div",{"id":"desc_content"}).text
        except:
            pass

        # extract the href attribute
        img_link = soup.find("div",{"class":"product-view-image-product"}).img['src']
        
        #Fill all information in class Book
        book.title = book_title
        book.price = book_price
        book.author = author_name
        book.translator = translator
        book.publisher = publisher
        book.num_pages = num_pages
        book.description = description_text
        book.image_url = img_link
        book.genere = self.genere

        return book.get_book_info()
        

