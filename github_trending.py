import requests
from datetime import date, timedelta


REPOSITORIES_COUNT = 20


def get_trending_repositories():
    url = 'https://api.github.com/search/repositories'
    week_ago = date.today() - timedelta(days=7)
    payload = {'q': 'created:>{}'.format(str(week_ago.isoformat())),
               'sort': 'stars', 'order': 'desc'}
    repositories = requests.get(url, params=payload).json()
    return repositories['items'][:REPOSITORIES_COUNT]


def output_repositories_to_console(repos):
    print('Trending repositories about this week.\n')
    for repo in sorted(repos, key=lambda repo: repo['stargazers_count'],
                       reverse=True):
        print('stars: {:<5} open issues: {:<3} {} {}'.format(str(repo['stargazers_count']),
                                                             str(repo['open_issues_count']),
                                                             repo['name'],
                                                             str(repo['html_url'])))


if __name__ == '__main__':
    output_repositories_to_console(get_trending_repositories())
