import requests
from bs4 import BeautifulSoup
import pprint

# get request for hacker news website
# change p = '' to any page number
res = requests.get('https://news.ycombinator.com/news?p=4')
# soup object
soup = BeautifulSoup(res.text, 'html.parser')

# grab all the title links
links = soup.select('.storylink')

# grab all the votes for the articles
subtext_votes = soup.select('.subtext')

# print(votes[0].get('id'))

def sort_stories_by_votes(hn_lists):
	return sorted(hn_lists, key= lambda k:k['votes'], reverse = True)

def create_custom_hn(links,subtext_votes):
	hn = []

	for index,item in enumerate(links):
		title = links[index].getText()
		href = links[index].get('href', None)
		vote = subtext_votes[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			if points > 99:
				hn.append({'title': title,'href':href, 'votes': points})
	return sort_stories_by_votes(hn)

# create_custom_hn(links,subtext_votes)
pprint.pprint(create_custom_hn(links,subtext_votes))