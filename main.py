#Import class Nhasachphuongnam
import pandas as pd
from loguru import logger
# from crawlers.nhasachphuongnam import Nhasachphuongnam
from crawlers.spiders import (
    Nhasachphuongnam,
    Tiki,
    Fahasa,
    Vinabook,
    Bookbuy
)
# from crawlers.models.book import Book
import csv, os

from urllib.parse import urlparse

df = pd.read_csv("book_collection.csv")
df.dropna(inplace = True) 
df.columns = ["Thể loại", "Nguồn nhập", "type"]

# fhs = Nhasachphuongnam('Van hoc duong dai',1,85)
# fhs.getBooks()

domain_functions = {
    # "nhasachphuongnam.com": Nhasachphuongnam,
    "tiki.vn": Tiki,
    "www.fahasa.com" : Fahasa,
    "www.vinabook.com": Vinabook,
    "bookbuy.vn":Bookbuy
}

# tiki = Tiki("https://tiki.vn/tac-pham-kinh-dien/c842",
#                 "Văn học kinh điển – cổ điển",
#                 1,2)
# result = tiki.getBooks()
# result = tiki.readBooks( (52789367, 52789368) )

# fahasa = Fahasa("https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc/tac-pham-kinh-dien.html?order=num_orders&limit=24&p=1",
#                 "Văn học kinh điển – cổ điển",
#                 1,2)
# result = fahasa.getBooks()
# result = fahasa.readBooks("https://www.fahasa.com/ong-gia-va-bien-ca-tai-ban-2018.html")

# vinabook = Vinabook("https://www.vinabook.com/c415/truyen-ngan-tan-van/",
#                     "Truyện ngắn - tản văn – tạp văn",
#                     1,2
# )
# result = vinabook.getBooks()
# result = vinabook.readBooks(" https://www.vinabook.com/mo-collection-vol1-p90349.html")

# bookbuy = Bookbuy("https://bookbuy.vn/sach/tac-pham-viet-nam-kinh-dien", 
#                   "Văn học kinh điển – cổ điển",
#                   1,2)
# result = bookbuy.getBooks()
# result = bookbuy.readBooks("https://bookbuy.vn/sach/dao-giau-vang-tai-ban-2020--p108259.html")
# logger.debug(result)

for idx,url in enumerate(df["Nguồn nhập"]):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    if domain in domain_functions:
        logger.debug(domain_functions[domain])
        process_func = domain_functions[domain]
        _func = process_func(url, df["Thể loại"][idx], 1, 1000)
        data = _func.getBooks()

        output_dir = 'outputs/' + domain

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logger.info(f"Directory {output_dir} created successfully!")


        output_file = output_dir+'/' + df["Thể loại"][idx] + '.csv'
        fieldnames = data[0].keys()
        with open(output_file, 'w', newline='', encoding='utf-8') as file:

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

            logger.success(f"CSV file {output_file} created successfully.")
    else:
        print("No processing function defined for domain:", domain)


# # Loop through the URLs and call the corresponding processing function based on the domain
# for url in urls:
#     parsed_url = urlparse(url)
#     domain = parsed_url.netloc

#     if domain in domain_functions:
#         process_func = domain_functions[domain]
#         process_func(url)
#     else:
#         print("No processing function defined for domain:", domain)