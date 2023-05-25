from crawlers.utils.requester import get_response
from bs4 import BeautifulSoup
from crawlers.models.book import Book
import csv

from loguru import logger

_category_path = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=100&include=advertisement&aggregations=1&category={}&page={}&urlKey={}"
_book_detail = 'https://tiki.vn/api/v2/products/{}?platform=web&spid={}'

class Tiki:

    def __init__(self, base_url, genere, page_num, page_max):
        self.base_url = base_url.replace(".html","")
        self.urlkey = urlkey
        self.category_name = genere

    def getBooks(self):
        booklinks=[]

        page_url = f"https://tiki.vn/api/personalish/v1/blocks/listings?limit=100&include=advertisement&aggregations=1&category={self.categoryid}&page=1&urlKey={self.urlkey}
        response = get_response(page_url).json()
        _total = response['paging']['last_page']+1

        
        for page_num in range(_total+1):
            page_num =+1

            page_url = f"https://tiki.vn/api/personalish/v1/blocks/listings?limit=100&include=advertisement&aggregations=1&category={self.categoryid}&page=1&urlKey={self.urlkey}
            response = get_response(page_url).json()

            for data in response['data']:
                booklinks.append( (data['id'],data['seller_product_id']) )

        bookRead = []
        for book in booklinks:
            logger.debug(f"Reading book: {book}")
            br = self.readBooks(book)
            bookRead.append(br)
            
    def readBooks(self, booklinks):
        response = get_response(booklinks)
        # parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        # initate new instance of class book with empty arguments
        book = Book('', '', '', '', '', '', '', '', '')
        # get book title
        # extract the book title
        book_title = soup.find('h1', class_='ty-mainbox-title').bdi.text
        # extract the book price
        book_price = soup.select_one('span[id*=discounted_price]').text

        # find all elements with class 'ty-product-feature'
        feature_elements = soup.find_all('div', class_='ty-product-feature')
        # loop through the elements and extract the values for specific labels
        
        num_pages = ''
        translator = ''
        publisher = ''
        author_name = ''
        num_pages = ''

        for feature in feature_elements:
            label = feature.find('span', class_='ty-product-feature__label')
            value = feature.find('div', class_='ty-product-feature__value')
            if label and value:
                if 'Số trang:' in label.text:
                    num_pages = value.text.strip()
                elif 'Dịch giả:' in label.text:
                    translator = value.text.strip()
                elif 'Nhà Xuất Bản:' in label.text:
                    publisher = value.text.strip()
                elif 'Tác giả:' in label.text:
                    author_name = value.text.strip()
                elif 'Số trang:' in label.text:
                    num_pages = value.text.strip()
        
        #Get book description
        description_section = soup.find('div', {'id': 'content_description'})
        description_text = description_section.get_text(strip=True)
      
        # find the <a> tag with id starting with "det_img_link"
        img_link_tag = soup.find('a', {'id': lambda x: x and x.startswith('det_img_link')})

        # extract the href attribute
        img_link = img_link_tag.get('href')

        print(img_link)

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
        

