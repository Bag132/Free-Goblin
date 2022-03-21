import requests

preflight_url = 'https://api.urbandictionary.com/v0/vote'
post_dislike_headers = {
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

if __name__ == '__main__':
	# send preflight
	print(requests.options(preflight_url, headers=post_dislike_headers).text)
