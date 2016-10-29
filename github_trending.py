import requests
from datetime import date, timedelta


def week_ago():
    today = date.today()
    return str(today - timedelta(days=7))


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    params = {'q': 'created:>' + week_ago(), 'sort': 'stars', 'order': 'desc'}
    response = requests.get(url, params=params)
    repos = response.json()['items'][:top_size]
    return [repo['full_name'] for repo in repos]


def collect_open_issues_links(repo_full_name):
    url = 'https://api.github.com/repos/{}/issues'.format(repo_full_name)
    response = requests.get(url).json()
    return ['\t' + link['url'] for link in response]


if __name__ == '__main__':
    trend_repos = get_trending_repositories(20)
    for name in trend_repos:
        user, repo = name.split('/')
        print('User: {}, repo: {}'.format(user, repo))
        issues = collect_open_issues_links(name)
        print('Issues amount: {}'.format(len(issues)))
        if len(issues) > 0:
            print('Links: ')
            print(*issues, sep='\n')
