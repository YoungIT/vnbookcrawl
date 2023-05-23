import requests
from urllib.error import HTTPError
import random
from requests_ip_rotator import ApiGateway

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
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
    print(f"Requesting {url}")
    #response = proxy_request(url)
    response = requests.get(url, headers=headers, timeout=5, verify=False)
    return response
