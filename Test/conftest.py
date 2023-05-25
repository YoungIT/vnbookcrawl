import pytest
from crawlers.spiders import (
    Tiki,
    Fahasa,
    Vinabook,
    Bookbuy
)
from crawlers.models.book import Book

@pytest.fixture
def book_model():

    book = Book('', '', '', '', '', '', '', '', '')

    return book

@pytest.fixture
def tiki_fixture():

    return Tiki("https://tiki.vn/tac-pham-kinh-dien/c842",
                "Văn học kinh điển – cổ điển",
                1,1)

@pytest.fixture
def lambda_b_instance():
    # Initialize the class or object needed for Lambda B
    return LambdaB()

@pytest.fixture
def lambda_c_instance():
    # Initialize the class or object needed for Lambda C
    return LambdaC()