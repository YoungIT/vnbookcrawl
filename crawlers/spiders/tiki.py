from crawlers.utils.requester import get_response
from bs4 import BeautifulSoup
from crawlers.models.book import Book
import csv

from loguru import logger

_category_path = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=100&include=advertisement&aggregations=1&category"
_book_detail = 'https://tiki.vn/api/v2/products'

class Tiki:

    def __init__(self, base_url, genere, page_num, page_max):

        self.base_url = base_url.replace(".html","")
        self.url_split = self.base_url.split("/")
        self.categoryid, self.urlkey = self.url_split[-1][1:], self.url_split[-2]
        self.category_name = genere
        self.page_num = page_num
        self.page_max = page_max

    def getBooks(self):
        booklinks=[]
        page_num = self.page_num
        page_max = self.page_max
        while page_num<page_max:

            page_url = f"{_category_path}={self.categoryid}&page=1&urlKey={self.urlkey}"
            response = get_response(page_url).json()

            if len(response['data']) == 0:
                break
            else:
                for data in response['data']:
                    booklinks.append( (data['id'],data['seller_product_id']) )

            page_num =+1

        bookRead = []
        for book in booklinks:
            logger.debug(f"Reading book: {book}")
            br = self.readBooks(book)
            bookRead.append(br)
            
    def readBooks(self, booklinks):

        book_id, seller_product_id = booklinks[0], booklinks[1]
        book_url = f"{_book_detail}/{book_id}?platform=web&spid={seller_product_id}"
        response = get_response(booklinks).json()
        # parse the HTML content using Beautiful Soup
        # initate new instance of class book with empty arguments
        book = Book('', '', '', '', '', '', '', '', '')
        # get book title
        # extract the book title
        book_title = response['price']
        # extract the book price
        book_price = response['price']
        # extract books's total pages
        num_pages = response['specifications'][0]['attributes'][5]['value']
        # extract publisher
        publisher = response['specifications'][0]['attributes'][0]['value']
        # extract translator
        translator = response['specifications'][0]['attributes'][3]['value']
        # extract authors
        author_name = ''

        for _author in response['authors']:
            author_name += _author['name'] + ','
        # loop through the elements and extract the values for specific labels
        
        #Get book description
        description_text = response['description']
      
        # find the <a> tag with id starting with "det_img_link"
        img_link = response['thumbnail_url']

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
        

