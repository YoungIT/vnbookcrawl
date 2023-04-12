# Book Scraper

This is a Python script for scraping book information from the sites like Nhasachphuongnam website. The script collects book titles, images, genres, authors, publishers, prices, descriptions, translators, and number of pages, and saves them to a CSV file.

## Requirements

To run this script, you will need:

- Python 3
- Beautiful Soup 4
- Requests

You can install the required libraries by running:

```
pip install beautifulsoup4 requests
```

## Usage

1. Clone this repository or download the ZIP file and extract it.

2. Navigate to the project directory in your terminal.

3. Run the `main.py` file using Python, and provide the genre, starting page, and ending page as arguments.

```
python main.py
```


This will scrape books in the "Van hoc duong dai" genre, starting from page 1 and ending at page 3. You can adjust these values to scrape books in a different genre or page range.

4. The script will output logs to the console as it scrapes book information. Once it has finished scraping, it will save the book data to a CSV file named `nhasachphuongnam.csv` in the project directory.


## Notes

- This script uses proxies to scrape the website. If you experience issues with scraping, you may need to update the proxies in the `proxylist.txt` file. If you do not wish to use proxies, you can modify the `proxy_request` function in `utils/requester.py` to remove the proxy parameter.
