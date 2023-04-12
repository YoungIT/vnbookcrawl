#import utils/requester
from crawlers.utils.requester import get_response
from bs4 import BeautifulSoup
#import class Book
from crawlers.models.book import Book
import csv
#init config constants
base_url = 'https://nhasachphuongnam.com/vi/van-hoc-duong-dai'


class Nhasachphuongnam:
   
    def __init__(self, genere, page_num, page_max):
        self.genere = genere
        self.page_num = page_num
        self.page_max = page_max
        pass

    def getBooks(self):
        booklinks=[]
        page_num = self.page_num
        page_max = self.page_max
        while page_num<page_max:
            
            page_url = f"{base_url}-page-{page_num}.html" if page_num > 1 else f"{base_url}.html"
            
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
                page_num=page_max
                break

            # increment the page number and continue to the next page
            page_num += 1
        
        bookRead = []
        for book in booklinks:
            print(f"Reading book: {book}")
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
        

