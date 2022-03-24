import time

import requests
from torpy import TorClient
from torpy.http.requests import TorRequests
from torpy.http.requests import tor_requests_session
from multiprocessing.pool import ThreadPool
from torpy.http.requests import tor_requests_session

preflight_url = 'https://api.urbandictionary.com/v0/vote'
preflight_headers = {
	'authority': 'api.urbandictionary.com',
	'accept': '*/*',
	'access-control-request-method': 'POST',
	'access-control-request-headers': 'content-type',
	'origin': 'https://www.urbandictionary.com',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'sec-fetch-dest': 'empty',
	'referer': 'https://www.urbandictionary.com/',
	'accept-language': 'en-US,en;q=0.9',
}

vote_payload = '{"defid": 16423887, "direction": "down"} '
vote_url = 'https://api.urbandictionary.com/v0/vote'
vote_headers = {
	'authority': 'api.urbandictionary.com',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
	'dnt': '1',
	'sec-ch-ua-mobile': '?0',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
	'sec-ch-ua-platform': '"Windows"',
	'content-type': 'application/json; charset=utf-8',
	'accept': '*/*',
	'origin': 'https://www.urbandictionary.com',
	'sec-fetch-site': 'same-site',
	'sec-fetch-mode': 'cors',
	'sec-fetch-dest': 'empty',
	'referer': 'https://www.urbandictionary.com/',
	'accept-language': 'en-US,en;q=0.9',
}


def send_dislike(id):
	with tor_requests_session() as sesh:
		print(sesh.options(preflight_url, headers=preflight_headers, timeout=5).text)
		payload = '{"defid": ' + str(id) + ', "direction": "down"}'
		print(sesh.post(vote_url, headers=vote_headers, data=payload, timeout=5).text)


def tor_bot():
	from multiprocessing.pool import ThreadPool

	elements = [id] * 3
	with ThreadPool(3) as pool:
		pool.map(send_dislike, elements)


def tor_basic():
	with tor_requests_session() as s:  # returns requests.Session() object
		print('IP: ' + str(s.get('https://httpbin.org/ip').json().))
		print(s.options(preflight_url, headers=preflight_headers).text)
		print(s.post(vote_url, headers=vote_headers, data=vote_payload).text)


def main():
	while True:
		tor_basic()
		time.sleep(1)


if __name__ == '__main__':
	main()
