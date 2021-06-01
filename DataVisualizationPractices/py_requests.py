import requests # Request package allows py program to easily request info from websites and examine the responses.

from plotly.graph_objs import Bar
from plotly import offline

# make an API call and store the response:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# see API rate limit: https://api.github.com/rate_limit
# most APIs are rate limited, a limit to # of requests we can make in a certain amount of time (min).

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
print(response_dict.keys())

print(f"\nTotal Repositories: {response_dict['total_count']}")
print(f"Repositories returned: {len(repo_dicts)}")

# examine the first repository:
first_repo = repo_dicts[0]
print("\nLet's take a look at the first repository returned:")
print(f"{len(first_repo)} keys as listed below:") # see how much info we have
for key in sorted(first_repo.keys()):
	print(f'\t{key}') # see what kind of info we have

# May easily get all following info by using for repo in repo_dicts.
print("\nSelected information about the first repository:")
print(f"\tName: {first_repo['name']}")
print(f"\tOwner: {first_repo['owner']['login']}")
print(f"\tStars: {first_repo['stargazers_count']}")
print(f"\tRepository: {first_repo['html_url']}")
print(f"\tCreated: {first_repo['created_at']}")
print(f"\tUpdated: {first_repo['updated_at']}")
print(f"\tDescription: {first_repo['description']}")

for repo in repo_dicts:
	repo_name = repo['name']
	repo_url = repo['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

	owner = repo['owner']['login']
	description = repo['description']

	# plotly allows HTML code within text elements, use <br /> to add line break:
	label = f"{owner}<br />{description}"

	labels.append(label)
	repo_links.append(repo_link)
	stars.append(repo['stargazers_count'])

data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(20, 140, 10)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': 'Most-Starred Pythan Projects on Github',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='web_pages/python_requests_repos.html')