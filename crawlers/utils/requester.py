import requests
from urllib.error import HTTPError
import random
from requests_ip_rotator import ApiGateway

requests.packages.urllib3.disable_warnings()

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
# }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,vi-VN;q=0.9,vi;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5,zh-CN;q=0.4,zh;q=0.3',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
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
def get_response(url, headers=headers):
    #response = proxy_request(url)
    response = requests.get(url, headers=headers, timeout=5, verify=False)
    return response
