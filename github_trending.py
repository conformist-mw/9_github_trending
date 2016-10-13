import requests
import datetime as DT


def week():
    today = DT.date.today()
    return str(today - DT.timedelta(days=7))


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    params = {'q': 'created:>' + week(), 'sort': 'stars', 'order': 'desc'}
    response = requests.get(url, params=params)
    repos = response.json()['items'][:top_size]
    # issues:
    d = {}
    for repo in repos:
        d[repo['name']] = repo['open_issues_count']
    return d


def get_open_issues_amount(repo_owner, repo_name):
    pass


if __name__ == '__main__':
    print(get_trending_repositories(5))
