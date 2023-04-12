# Define class Book
# Class book has properties: title, image_url, genere, author, publisher, price, description
# Class book has methods: get_title, get_image_url, get_genere, get_author, get_publisher, get_price, get_description
# Class book has method: get_book_info
# Class book has method: get_book_info_from_url
class Book:
    def __init__(self, title, image_url, genere, author, publisher, price, description, translator,num_pages):
        self.title = title
        self.image_url = image_url
        self.genere = genere
        self.author = author
        self.publisher = publisher
        self.price = price
        self.description = description
        self.translator = translator
        self.nup_pages = num_pages

    def get_title(self):
        return self.title

    def get_image_url(self):
        return self.image_url

    def get_genere(self):
        return self.genere

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description
    
    def get_translator(self):
        return self.translator

    def get_num_pages(self):
        return self.num_pages

    def get_book_info(self):
        return {
            'title': self.title,
            'image_url': self.image_url,
            'genere': self.genere,
            'author': self.author,
            'publisher': self.publisher,
            'price': self.price,
            'description': self.description,
            'translator': self.translator,
            'num_pages': self.num_pages
        }

