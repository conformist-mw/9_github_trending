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
    return [repo['full_name'] for repo in repos]


def get_open_issues_amount(full_name):
    url = 'https://api.github.com/repos/{}/issues'.format(full_name)
    response = requests.get(url).json()
    issues = ['\t' + link['url'] for link in response]
    return issues


if __name__ == '__main__':
    repo_names = get_trending_repositories(20)
    for name in repo_names:
        user, repo = name.split('/')
        print('User: {}, repo: {}'.format(user, repo))
        issues = get_open_issues_amount(name)
        print('Issues amount: {}'.format(len(issues)))
        if len(issues) > 0:
            print('Links: ')
            print(*issues, sep='\n')
