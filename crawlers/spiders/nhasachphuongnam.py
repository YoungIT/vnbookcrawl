from crawlers.utils.requester import get_response
from bs4 import BeautifulSoup
from crawlers.models.book import Book
import csv

from loguru import logger

class Nhasachphuongnam:
   
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
            
            page_url = f"{self.base_url}-page-{page_num}.html" if page_num > 1 else f"{self.base_url}.html"
            
            response = get_response(page_url)
            # parse the HTML content using Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')

            # find all the book links and append them to the list
            for link in soup.find_all('a', class_='product-title'): 
                #log added link
                print(f"Added link: {link['href']}")
                booklinks.append(link['href'])

            # check if the response header contains the HTML code indicating a 404 error
            if '404' in response.headers.get('content-type'):
                break

            if page_num == page_max:
                break

            # increment the page number and continue to the next page
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
        # initate new instance of class book with empty arguments
        book = Book('', '', '', '', '', '', '', '', '')
        # get book title
        # extract the book title
        book_title = soup.find('h1', class_='ty-mainbox-title').bdi.text
        # extract the book price
        book_price = soup.select_one('span[id*=discounted_price]').text

        # extract book's total page
        num_pages = _soup.find('span', itemprop='numberOfPages').get_text(strip=True)

        # extract translater
        translator = _soup.find('span', itemprop='editor').get_text(strip=True)

        # extract publisher
        publisher = _soup.find('span', class_='publishers').get_text(strip=True)

        # extract book's author
        author_name = _soup.find('span', class_='author').get_text(strip=True)

        description_section = soup.find('div', {'id': 'content_description'})
        description_text = soup.find("div",{"class":"full-description"}).text.split("...")[0]
      
        # extract the href attribute
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
        

