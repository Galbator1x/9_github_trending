import requests
from datetime import date, timedelta


def get_trending_repositories():
    d = date.today() - timedelta(days=7)
    url = 'https://api.github.com/search/repositories?q=created:%3E{}&sort=stars&order=desc'. \
        format(str(d.isoformat()))
    repositories = requests.get(url).json()
    trending_repos = {}
    for repo in repositories['items'][:20]:
        name = repo['name']
        trending_repos[name] = {'owner': repo['owner']['login'],
                                'stars': repo['stargazers_count'],
                                'repo_url': repo['html_url'],
                                'issues': repo['open_issues_count']}

    return trending_repos


if __name__ == '__main__':
    repos = get_trending_repositories()
    print('Trending repositories about this week.\n')
    for repo_name, repo in sorted(repos.items(),
                                  key=lambda repo: repo[1]['stars'],
                                  reverse=True):
        print('{:-<40} stars: {:-<10} open issues: {:-<5} {}'.format(repo_name,
                                                                     str(repo['stars']),
                                                                     str(repo['issues']),
                                                                     str(repo['repo_url'])))
