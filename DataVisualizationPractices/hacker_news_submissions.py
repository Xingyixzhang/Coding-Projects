### TO DOs:
#	1. Use other languages to try the same program functionality
#	2. Make Unit tests for this program
#	3. Active Discussion chart using plotly

from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status Code: {r.status_code}')

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
	url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
	r = requests.get(url)
	print(f"ID: {submission_id}\tStatus Code: {r.status_code}")
	response_dict = r.json()

	submission_dict = {
		'title': response_dict['title'],
		'hn-link': f'https://news.ycombinator.com/item?id={submission_id}',
		# 'comments': response_dict['descendants'],
	}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('title'), reverse=True)

for submission_dict in submission_dicts:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion Link: {submission_dict['hn-link']}")
	# print(f"Comments: {submission_dict['comments']}")