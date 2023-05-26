from ..utils.requester import get_response
from bs4 import BeautifulSoup
from ..models.book import Book
import csv

from loguru import logger

class Vinabook:
   
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
            
            page_url = f"{self.base_url}page-{page_num}"

            response = get_response(page_url)
            soup = BeautifulSoup(response.text, "html.parser")
        
            for link in soup.findAll("p",{"class":"price-info-nd"}):
                logger.debug(link.a['href'].rstrip())
                booklinks.append(link.a['href'].rstrip())

            if "Không có sản phẩm" in response.text:

                break

            if page_num == page_max:
                
                break

            page_num += 1
        
        # return booklinks
            
        bookRead = []
        for book in booklinks:
            logger.debug(f"Reading book: {book}")
            br = self.readBooks(book)
            bookRead.append(br)

        # print("Successfuly taken all book")
        #write bookRead list to csv file
        # with open('nhasachphuongnam.csv', 'w', newline='', encoding='utf-8') as file:
            # writer = csv.writer(file)
            # writer.writerow(['title', 'image_url', 'genere', 'author', 'publisher', 'price', 'description', 'translator', 'num_pages'])
            # for book in bookRead:
            #     writer.writerow([book.title, book.image_url, book.genere, book.author, book.publisher, book.price, book.description, book.translator, book.num_pages])

    def readBooks(self, booklinks):

        headers = {
            'authority': 'www.vinabook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en,vi-VN;q=0.9,vi;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5,zh-CN;q=0.4,zh;q=0.3',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        response = get_response(booklinks, headers)
        # parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        # initate new instance of class book with empty arguments
        book = Book('', '', '', '', '', '', '', '', '')

        # extract the book title
        book_title = soup.h1.text

        # extract the book price
        book_price = soup.find("span",{"class":"list-price nowrap"}).text

        num_pages = ''
        translator = ''
        publisher = ''
        author_name = ''
        num_pages = ''

        author_tag = soup.find('strong', text='Tác giả: ')
        if author_tag:
            author_name = author_tag.find_next_sibling('span', class_='author').get_text(strip=True)

        publisher_tag = soup.find('strong', text='Nhà xuất bản: ')
        if publisher_tag:
            publisher = publisher_tag.find_next_sibling('span', class_='publishers').get_text(strip=True)

        num_pages_tag = soup.find('strong', text='Số trang: ')
        if num_pages_tag:
            num_pages = num_pages_tag.find_next_sibling('span', itemprop='numberOfPages').get_text(strip=True)
                
        #Get book description
        description_text = soup.find('div',class_='mainbox2-container').text
      
        # find the <a> tag with id starting with "det_img_link"
        img_tag = soup.find('img', itemprop='image')

        # extract the href attribute
        if img_tag:
            img_link = img_tag['src']

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
        

