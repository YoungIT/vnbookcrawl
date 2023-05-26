import pytest
from ..crawlers.spiders import (
    Tiki,
    Fahasa,
    Vinabook,
    Bookbuy
)
from ..crawlers.models.book import Book

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
def fahasa_fixture():
    return Fahasa()

@pytest.fixture
def vinabook_fixture():
    return Vinabook()

@pytest.fixture
def bookbuy_fixture():
    return Bookbuy()