import unicodedata
from crawlers.utils.requester import get_response
import pandas as pd
from bs4 import BeautifulSoup
from crawlers.models.book import Book
import csv

from loguru import logger

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

            page_url = f"{self.base_url}?order=num_orders&limit=24&p={page_num}"

            response = get_response(page_url)
            soup = BeautifulSoup(response.content, 'html.parser')

            for link in soup.findAll("h2",{"class":"product-name-no-ellipsis p-name-list"}):
                booklinks.append(link.a['href'])

            if "Không có sản phẩm phù hợp với từ khóa tìm kiếm của bạn." in response.text:

                break

            page_num += 1
        
        bookRead = []
        for book in booklinks:
            logger.debug(f"Reading book: {book}")
            br = self.readBooks(book)
            bookRead.append(br)

        print("Successfuly taken all book")
        #write bookRead list to csv file
        with open('nhasachphuongnam.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'image_url', 'genere', 'author', 'publisher', 'price', 'description', 'translator', 'num_pages'])
            for book in bookRead:
                writer.writerow([book.title, book.image_url, book.genere, book.author, book.publisher, book.price, book.description, book.translator, book.num_pages])

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
        book_title = re.sub("(?m)^\s+","", _soup.h1.text.rstrip())

        # extract the book price
        book_price = unicodedata.normalize("NFKD",_soup.findAll("span",{"class":"price"})[-1].text)

        # extract book's author
        author_name = df[1][df.index[df[0].str.contains("Tác giả")].to_list()[0]]

        # extract translater
        translator = ''
        try:
            translator = df[1][df.index[df[0].str.contains("Người Dịch")].to_list()[0]]
        except:
            pass

        # extract publisher
        publisher = df[1][df.index[df[0].str.contains("NXB")].to_list()[0]]

        # extract book's total page
        num_pages = df[1][df.index[df[0].str.contains("Số trang")].to_list()[0]]

        # get book description
        description_text = soup.find("div",{"id":"desc_content"}).text

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

        return book
        

