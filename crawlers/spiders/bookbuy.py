import re

from ..utils.requester import get_response
from bs4 import BeautifulSoup
from ..models.book import Book
import csv

from loguru import logger

class Bookbuy:
   
    def __init__(self, base_url, genere, page_num, page_max):
        self.base_url = base_url.replace(".html","")
        self.genere = genere
        self.page_num = page_num
        self.page_max = page_max

    def getBooks(self):
        booklinks=[]
        page_num = self.page_num
        page_max = self.page_max
        while page_num<page_max:

            logger.info(f"Crawling Page {page_num} of {self.base_url}")
            
            page_url = f"{self.base_url}?Page={page_num}"
            
            response = get_response(page_url)
            # parse the HTML content using Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')
            book_div = soup.find_all('div', class_='t-view')
            if len(book_div) == 0:
                break
            else:
                # find all the book links and append them to the list
                for link in book_div:
                    try:
                        booklinks.append("https://bookbuy.vn"+link.a['href'])
                    except:
                        pass

            # check if the response header contains the HTML code indicating a 404 error
            
            if page_num == page_max:

                break

            # increment the page number and continue to the next page
            page_num += 1

        # return booklinks
        
        bookRead = []
        for book in booklinks:
            try:
                logger.debug(f"Reading book: {book}")
                br = self.readBooks(book)
                bookRead.append(br)
            except:
                pass
        #write bookRead list to csv file
        # with open('nhasachphuongnam.csv', 'w', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(['title', 'image_url', 'genere', 'author', 'publisher', 'price', 'description', 'translator', 'num_pages'])
        #     for book in bookRead:
        #         writer.writerow([book.title, book.image_url, book.genere, book.author, book.publisher, book.price, book.description, book.translator, book.num_pages])

    def readBooks(self, booklink):

        response = get_response(booklink)
        soup = BeautifulSoup(response.content, 'html.parser')

        book = Book('', '', '', '', '', '', '', '', '')
        # extract book title
        book_title = soup.find('h1', class_='title').text
        # extract the book price
        book_price = soup.find('p', class_='price').text
        # extract book's author
        author_name =''
        author_list = soup.find('div',class_='author-list')
        if author_list is not None:
            author_name = soup.find('h2', class_='author').text
        # extract translater
        translator = ''
        tran_list = soup.find('div',class_='tran-list')
        if tran_list is not None:
            for i in translator.findAll("h2"):
                translator += i.text.rstrip() +','

        # extract Features 
        feature = soup.findAll('li',class_='item-p')
        # extract publisher
        publisher = ''
        try:
            publisher = feature[0].a.text.strip()
        except:
            pass
        # extract book's total page
        num_pages = ''
        try:
            num_pages = re.sub('[^A-Za-z0-9]+', ' ', feature[4].find('span').text)
        except:
            pass

        #Get book description
        description_section = soup.find('div', class_='des-des')
        description_text = description_section.get_text(strip=True)
        # extract the href attribute
        img_link = soup.find('div',class_='product-zoom slimmage')

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
        

