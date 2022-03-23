import requests


def preflight(sesh) -> requests.Response():
	preflight_url = 'https://api.urbandictionary.com/v0/vote'
	preflight_headers = {
		'authority': 'api.urbandictionary.com',
		'accept': '*/*',
		'access-control-request-method': 'POST',
		'access-control-request-headers': 'content-type',
		'origin': 'https://www.urbandictionary.com',
		# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
		'user-agent': 'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'sec-fetch-dest': 'empty',
		'referer': 'https://www.urbandictionary.com/',
		'accept-language': 'en-US,en;q=0.9',
	}
	return sesh.options(preflight_url, headers=preflight_headers, timeout=5)


def vote(sesh, entry_id, direction) -> requests.Response():
	vote_payload = '{"defid": ' + str(entry_id) + ', "direction": "' + str(direction) + '"} '
	vote_url = 'https://api.urbandictionary.com/v0/vote'
	vote_headers = {
		'authority': 'api.urbandictionary.com',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
		'dnt': '1',
		'sec-ch-ua-mobile': '?0',
		# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
		'user-agent': 'Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1',
		'sec-ch-ua-platform': '"Android"',
		'content-type': 'application/json; charset=utf-8',
		'accept': '*/*',
		'origin': 'https://www.urbandictionary.com',
		'sec-fetch-site': 'same-site',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://www.urbandictionary.com/',
		'accept-language': 'en-US,en;q=0.9',
	}

	return sesh.post(vote_url, headers=vote_headers, data=vote_payload, timeout=5)


if __name__ == '__main__':
	session = requests.Session()
	session.proxies = {
		"http": 'http://188.138.11.39:5566',
		"https": 'http://188.138.11.39:5566'
	}

	# send preflight
	print(preflight(session).text)

	# send vote
	vote_response = vote(session, '16423887', 'down')
	print(vote_response.text)
