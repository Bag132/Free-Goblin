from email.policy import default
import re
import time
import sys
from tkinter import FALSE
import requests
import argparse
import torpy.keyagreement
from multiprocessing.pool import ThreadPool
from torpy.http.requests import tor_requests_session

vote_url = 'https://api.urbandictionary.com/v0/vote'
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

upvotes = [0]
downvotes = [0]


def vote(sesh, defid, up):
	# Send vote
	direction = 'up' if up else 'down'
	payload = '{"defid": ' + str(defid) + ', "direction": "' + direction + '"}'
	response = sesh.post(vote_url, headers=vote_headers, data=payload, timeout=5).json()
	status = response['status']

	# Display finished status of vote
	if status != 'challenge':
		if up:
			upvotes[0] = upvotes[0] + 1
			print(f'{defid} Up: {response["up"]}, Down: {response["down"]} | Saved | Upvotes: {upvotes[0]}')
		else:
			downvotes[0] = downvotes[0] + 1
			print(f'{defid} Up: {response["up"]}, Down: {response["down"]} | Saved | Downvotes: {downvotes[0]}')
	else:
		print(str(defid) + ' Challenged')


def like_worker(ids):
	upID = ids[0]
	downID = ids[1]
	# print(f'upID = {upID}\ndownID = {downID}')
	if downID is None and upID is None:
		return

	while True:
		# Ignore all torpy errors
		try:
			# Generate new tor session
			with tor_requests_session() as sesh:
				# print('IP: ' + str(sesh.get('https://httpbin.org/ip').json()['origin']))
				sesh.options(vote_url, headers=preflight_headers, timeout=5)
				time.sleep(0.075)

				if upID is not None:
					vote(sesh, upID, True)

				if downID is not None:			
					vote(sesh, downID, False)

		except Exception:
			pass
		time.sleep(3)


def send_likes(likeID:str = None, dislikeID:str = None, threads:int = 1) -> None:
	"""Starts multiple threads to send likes to a likeID or dislikeID

	Args:
		likeID (str): Definition ID to send likes to 
		dislikeID (str): Definition ID to send dislikes to 
		threads (int): Number of threads to create for sending likes or dislikes
	"""

	pool = ThreadPool(threads)
	# For every ID tuple assign a new like worker to the arguments
	# Blocking call
	pool.map(like_worker, [(likeID, dislikeID)] * threads)
	

# '15108537' 17012584  16423887
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--up', '-u', required=False, help='Definition ID to like')
	parser.add_argument('--down', '-d', required=False, help='Definition ID to dislike')
	parser.add_argument('--threads', '-t', required=False, help='Number of threads to use', default='2')
	args = parser.parse_args()

	if not args.up and not args.down:
		parser.print_help(sys.stderr)
		exit(1)

	print(f'Sending likes to {args.up} and dislikes to {args.down} with {args.threads} threads')

	# Renew threads if they fail
	while True:
		send_likes(likeID=args.up, dislikeID=args.down, threads=int(args.threads))


