import requests
import time

preflight_url = 'https://api.urbandictionary.com/v0/vote'
preflight_headers = {
	'authority': 'api.urbandictionary.com',
	'accept': '*/*',
	'access-control-request-method': 'POST',
	'access-control-request-headers': 'content-type',
	'origin': 'https://www.urbandictionary.com',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
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
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
	'sec-ch-ua-platform': '"Windows"',
	'content-type': 'application/json; charset=utf-8',
	'accept': '*/*',
	'origin': 'https://www.urbandictionary.com',
	'sec-fetch-site': 'same-site',
	'sec-fetch-mode': 'cors',
	'sec-fetch-dest': 'empty',
	'referer': 'https://www.urbandictionary.com/',
	'accept-language': 'en-US,en;q=0.9',
	# Requests sorts cookies= alphabetically
	# 'cookie': '_ga=GA1.2.929289410.1647897903; _li_dcdm_c=.urbandictionary.com; _lc2_fpi=7b1bfe6a19f7--01fyq5x06490ppx3c73b0cdrbv; _gid=GA1.2.1560578189.1648003577; __qca=I0-1493211718-1648004540664; cto_bundle=oSTGYF9wVVNWZXN5UWdMMHpmWkhsJTJCZEdhaUQlMkY4T3JrYzlnUUtVJTJCc1JIYlRad0JVJTJGcTc3REdvemhJa1EwZHBrS2NpbHZTYVl0YWExWXNXYXFMU2l4SmVwTHVqMUpGVmtEd0V1R3N2NUwlMkZFeUFISzREZ3FNNnRORERIbXZBMSUyQnBRNWFQWkFxaGNuRjdKRjlEVUtDUzZwb0FYWHB1d2dmclMxVzVuR0hYVVdpWXlQbWslM0Q',
}
vote_cookie = {
	'_ga': 'GA1.2.929289410.1647897903',
	'_li_dcdm_c': '.urbandictionary.com',
	'_lc2_fpi': '7b1bfe6a19f7--01fyq5x06490ppx3c73b0cdrbv',
	'_gid': 'GA1.2.1560578189.1648003577',
	'__qca': 'I0-1493211718-1648004540664',
	'cto_bundle': 'oSTGYF9wVVNWZXN5UWdMMHpmWkhsJTJCZEdhaUQlMkY4T3JrYzlnUUtVJTJCc1JIYlRad0JVJTJGcTc3REdvemhJa1EwZHBrS2NpbHZTYVl0YWExWXNXYXFMU2l4SmVwTHVqMUpGVmtEd0V1R3N2NUwlMkZFeUFISzREZ3FNNnRORERIbXZBMSUyQnBRNWFQWkFxaGNuRjdKRjlEVUtDUzZwb0FYWHB1d2dmclMxVzVuR0hYVVdpWXlQbWslM0Q',
}
if __name__ == '__main__':
	session = requests.Session()

	# send preflight
	start_time = time.time()
	preflight_response = session.options(preflight_url, headers=preflight_headers)
	print("Time after preflight: " + str(time.time() - start_time))
	print('Preflight Headers: ' + str(preflight_response.headers.values()))
	print('Preflight Cookies: ' + str(preflight_response.cookies.get_dict()))
	print('Preflight text: ' + str(preflight_response.text))
	# send vote
	vote_response = session.post(vote_url, headers=vote_headers, cookies=vote_cookie, data=vote_payload, timeout=5)
	print(vote_response.text)
	print("Time after vote: " + str(time.time() - start_time))
