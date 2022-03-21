import requests
import time

preflight_url = 'https://api.urbandictionary.com/v0/vote'
preflight_headers = {
	'authority': 'api.urbandictionary.com',
	'method': 'OPTIONS',
	'path': '/v0/vote',
	'scheme': 'https',
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'access-control-request-headers': 'content-type',
	'access-control-request-method': 'POST',
	'origin': 'https://www.urbandictionary.com',
	'referer': 'https://www.urbandictionary.com/',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}

vote_payload = '{defid: 16423887, direction: "down"} '
vote_url = 'https://api.urbandictionary.com/v0/vote'
vote_headers = {
	'authority': 'api.urbandictionary.com',
	'method': 'OPTIONS',
	'path': '/v0/vote',
	'scheme': 'https',
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'content-length': str(len(vote_payload)),
	'content-type': 'application/json; charset=utf-8',
	'cookie': '_ga=GA1.2.929289410.1647897903; _gid=GA1.2.1279202208.1647897903; _li_dcdm_c=.urbandictionary.com; _lc2_fpi=7b1bfe6a19f7--01fyq5x06490ppx3c73b0cdrbv; cto_bundle=6pTutl9wVVNWZXN5UWdMMHpmWkhsJTJCZEdhaUwlMkZhSmFZaG5ERG4za3R4Y0xVOUNYenVWV0xqSVFld3JDcUlmN21teHNsdVRRZnZ5cGVWSjBGRzNkczJ5c3FGQlBWbUtxVSUyRkNIQjZKSTBJVVBGZDFwYUtCbXQxWldjdlJhbTd0VEc4Y1FrSndMVVBaMHglMkZWQTFIT09FWjIzQmhzZzNuUnhqcXBuR0tsdGtxQmhESmxhRSUzRA',
	'dnt': '1',
	'origin': 'https://www.urbandictionary.com',
	'referer': 'https://www.urbandictionary.com/',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
vote_cookie = {
	'_li_dcdm_c=': '.urbandictionary.com',
}
if __name__ == '__main__':
	# send preflight
	print(requests.options(preflight_url, headers=preflight_headers).text)
	# time.sleep(0.5)
	# send vote
	print(requests.post(vote_url, headers=vote_headers).text)
