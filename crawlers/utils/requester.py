import requests
from urllib.error import HTTPError
import random
from requests_ip_rotator import ApiGateway

requests.packages.urllib3.disable_warnings()

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
# }

headers = {
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
      'sec-ch-ua-platform': '"Windows"',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,vi-VN;q=0.7',
    }

class API_Gateway_rotater:
    def __init__(self, url, AWS_ID, AWS_SECRET):
        self.gateway = ApiGateway(url, 
                    access_key_id=AWS_ID, 
                    access_key_secret=AWS_SECRET)
        self.gateway.start(force=True)

    def _close_gw(self):

        self.gateway.shutdown()

#get response from url
# @decorators.retry(HTTPError, delay=5, tries=3, logger=logger)
def get_response(url):
    #response = proxy_request(url)
    response = requests.get(url, headers=headers, timeout=5, verify=False)
    return response
