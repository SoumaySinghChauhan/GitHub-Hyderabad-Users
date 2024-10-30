import requests
import csv
import time

GITHUB_TOKEN = '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'  # Replace with your GitHub token
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

def fetch_users(location="Hyderabad", min_followers=50):
    url = f"https://api.github.com/search/users?q=location:{location}+followers:>{min_followers}"
    response = requests.get(url, headers=HEADERS)
    users_data = response.json().get('items', [])
    return users_data

def fetch_user_details(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def fetch_repos(username):
    repos = []
    page = 1
    while page <= 5:  # Adjust page count to limit requests for up to 500 repos
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)
        repos.extend(response.json())
        page += 1
        time.sleep(1)  # Respect GitHub API rate limits
    return repos

def clean_company_name(company):
    if company:
        company = company.strip().lstrip('@').upper()
    return company

def create_users_csv(users):
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at'])
        for user in users:
            user_details = fetch_user_details(user['login'])
            writer.writerow([
                user['login'],
                user_details.get('name', ''),
                clean_company_name(user_details.get('company', '')),
                user_details.get('location', ''),
                user_details.get('email', ''),
                user_details.get('hireable', ''),
                user_details.get('bio', ''),
                user_details.get('public_repos', 0),
                user_details.get('followers', 0),
                user_details.get('following', 0),
                user_details.get('created_at', '')
            ])

def create_repositories_csv(users):
    with open('repositories.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name'])
        for user in users:
            repos = fetch_repos(user['login'])
            for repo in repos[:500]:  # Limit to 500 repositories
                writer.writerow([
                    user['login'],
                    repo['full_name'],
                    repo['created_at'],
                    repo.get('stargazers_count', 0),
                    repo.get('watchers_count', 0),
                    repo.get('language', ''),
                    repo.get('has_projects', ''),
                    repo.get('has_wiki', ''),
                    repo['license']['name'] if repo.get('license') else ''
                ])

# Fetch users and save to CSV
users = fetch_users()
create_users_csv(users)
create_repositories_csv(users)
