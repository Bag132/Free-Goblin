import time

import requests
import torpy.keyagreement
from multiprocessing.pool import ThreadPool
import threading
from torpy.http.requests import tor_requests_session

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
}


# def dislike_worker(did):
# 	with tor_requests_session() as sesh:
# 		print('IP: ' + str(sesh.get('https://httpbin.org/ip').json()['origin']))
# 		print(sesh.options(preflight_url, headers=preflight_headers, timeout=5).text)
# 		payload = '{"defid": ' + str(did) + ', "direction": "down"}'
# 		print(sesh.post(vote_url, headers=vote_headers, data=payload, timeout=5).text)

def dislike_worker(defid):
	while True:
		try:
			with tor_requests_session() as sesh:
				# print('IP: ' + str(sesh.get('https://httpbin.org/ip').json()['origin']))
				sesh.options(preflight_url, headers=preflight_headers, timeout=5)
				time.sleep(0.075)
				payload = '{"defid": ' + str(defid) + ', "direction": "down"}'
				vote_response = sesh.post(vote_url, headers=vote_headers, data=payload, timeout=5).json()
				vote_status = vote_response['status']
				if vote_status != 'challenge':
					print("Up: " + str(vote_response['up']) + ', Down: ' + str(vote_response['down']) + ' | Saved')
				else:
					print(str(defid) + 'Challenged')
		except Exception:
			pass
		time.sleep(3)


def send_dislike(did):
	ids = [did, did, did]
	with ThreadPool(3) as pool:
		pool.map(dislike_worker, ids)


def like_worker(defid):
	downdefid = '16423887'
	while True:
		try:
			with tor_requests_session() as sesh:
				# print('IP: ' + str(sesh.get('https://httpbin.org/ip').json()['origin']))
				sesh.options(preflight_url, headers=preflight_headers, timeout=5)
				time.sleep(0.075)
				payload = '{"defid": ' + str(defid) + ', "direction": "up"}'
				down_payload = '{"defid": ' + str(downdefid) + ', "direction": "down"}'
				vote_response = sesh.post(vote_url, headers=vote_headers, data=payload, timeout=5).json()
				downvote_response = sesh.post(vote_url, headers=vote_headers, data=down_payload, timeout=5).json()
				vote_status = vote_response['status']
				downvote_status = downvote_response['status']

				if vote_status != 'challenge':
					print(str(defid) + " Up: " + str(vote_response['up']) + ', Down: ' + str(vote_response['down']) + ' | Saved')
				else:
					print(str(defid) + ' Challenged')

				if downvote_status != 'challenge':
					print(str(downdefid) + " Up: " + str(downvote_response['up']) + ', Down: ' + str(downvote_response['down']) + ' | Saved')
				else:
					print(str(downdefid) + ' Challenged')

		except Exception:
			pass
		time.sleep(3)


def send_like(defid, threads=3):
	pool = ThreadPool(threads)
	pool.map(like_worker, [defid] * threads)


def main():
	while True:
		try:
			send_like('15108537', threads=5)
			# send_dislike('16423887', threads=5)
		# 				send_like('17012584', threads=3)
		except requests.exceptions.ReadTimeout:
			pass
		except requests.exceptions.ConnectTimeout:
			pass
		except torpy.keyagreement.KeyAgreementError:
			pass
		except torpy.circuit.CellTimeoutError:
			pass
		except torpy.cell_socket.TorSocketConnectError:
			pass
		except Exception:
			print('Error')


if __name__ == '__main__':
	main()
