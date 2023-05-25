#Import class Nhasachphuongnam
import pandas as pd
from loguru import logger
# from crawlers.nhasachphuongnam import Nhasachphuongnam
from crawlers.spiders import (
    Nhasachphuongnam
)

from urllib.parse import urlparse

df = pd.read_csv("book_collection.csv")
df.dropna(inplace = True) 
df.columns = ["Thể loại", "Nguồn nhập", "type"]

# fhs = Nhasachphuongnam('Van hoc duong dai',1,85)
# fhs.getBooks()

domain_functions = {
    "nhasachphuongnam.com": Nhasachphuongnam,
    # "tiki.vn": tiki,
    # "www.fahasa.com" : Fahasa,
    # "www.vinabook.com": Vinabook,
    # "bookbuy.vn":Bookbuy
}

domain = "nhasachphuongnam.com"
process_func = domain_functions[domain]
_func = process_func("https://nhasachphuongnam.com/vi/van-hoc-duong-dai.html", df["Thể loại"][1], 1, 4)
_func.getBooks()

# for idx,url in enumerate(df["Nguồn nhập"]):
#     parsed_url = urlparse(url)
#     domain = parsed_url.netloc

#     if domain in domain_functions:
#         logger.debug(domain_functions[domain])
#         process_func = domain_functions[domain]
#         _func = process_func(url, df["Thể loại"][idx], 1, 2)
#         _func.getBooks()

#         break
#     else:
#         print("No processing function defined for domain:", domain)


# # Loop through the URLs and call the corresponding processing function based on the domain
# for url in urls:
#     parsed_url = urlparse(url)
#     domain = parsed_url.netloc

#     if domain in domain_functions:
#         process_func = domain_functions[domain]
#         process_func(url)
#     else:
#         print("No processing function defined for domain:", domain)