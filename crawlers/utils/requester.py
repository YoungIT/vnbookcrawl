import requests
import random
import socks
import socket
#config headers
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

# rotate proxy in proxylist.txt
def rotate_proxy():
    with open('proxylist.txt', 'r') as f:
        proxies = f.readlines()
        # return random proxy in the list
        return proxies[random.randint(0, len(proxies) - 1)].strip()


#proxy request
def proxy_request(url):
    
    while True:
    #request and retry with another proxy if proxy not work
        try:
            # get the next proxy
            proxy = rotate_proxy()
            # split the proxy string into host and port
            host, port = proxy.split(':')
            # set the default socket timeout to 5 seconds
            socket.setdefaulttimeout(5)
            # create a socks5 proxy connection
            socks.set_default_proxy(socks.SOCKS5, host, int(port))
            socket.socket = socks.socksocket
            # make the request using the socks5 proxy
            print(f"Requesting {url} with proxy {proxy}")
            response = requests.get(url, headers=headers, timeout=5, verify=False)
            # print log response
            print(f"Response {response.status_code}")
            return response
        # catch exeption, print error
        except Exception as e:
            print(f"Error: {e}")
            continue


#get response from url
def get_response(url):
    print(f"Requesting {url}")
    #response = proxy_request(url)
    response = requests.get(url, headers=headers, timeout=5, verify=False)
    return response
