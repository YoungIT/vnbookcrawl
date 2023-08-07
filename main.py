import pandas as pd
from loguru import logger
from crawlers.spiders import (
    Nhasachphuongnam,
    Tiki,
    Fahasa,
    Vinabook,
    Bookbuy
)
import csv, os
from urllib.parse import urlparse
import optparse

logger.add("debug.log")

def crawl(input_file):
    domain_functions = {
        "nhasachphuongnam.com": Nhasachphuongnam,
        "tiki.vn": Tiki,
        "www.fahasa.com" : Fahasa,
        "www.vinabook.com": Vinabook,
        "bookbuy.vn":Bookbuy
    }

    df = pd.read_csv(input_file)
    df.dropna(inplace = True) 
    df.columns = ["STT", "Thể loại", "Nguồn nhập"]

    for idx,url in enumerate(df["Nguồn nhập"]):
            try:
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
            except Exception as Error:
                logger.debug(f"cannot crawl {url} due to Error : {Error}")

def main():

    parser = optparse.OptionParser()
     
    parser.add_option('-f', dest = 'file',
                      type = 'str',
                      help = 'File csv for crawl')
     
    (options, args) = parser.parse_args()

    crawl(options.file)    

if __name__ == '__main__':
    main()