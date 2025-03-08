import requests
from colorama import Fore, init, Style
import os
import datetime
from collections import Counter

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_repositories(username):
    url = f'https://api.github.com/users/{username}/repos?per_page=100'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None
    
    repos = response.json()
    return repos

def get_pinned_repos(username):
    url = f"https://github.com/{username}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    pinned_repos = soup.find_all('span', class_='repo')

    return [repo.text.strip() for repo in pinned_repos]

def github_parser(username):
    url = f'https://api.github.com/users/{username}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Error: This profie doesn't exists or request failed")
        return

    user = data.get('login') or "Unknown"
    name = data.get('name') or "Unknown"
    bio = data.get('bio') or 'No bio available'
    location = data.get('location') or 'Unknown'
    email = data.get('email') or 'Not available'
    blog = data.get('blog') or 'Not available'
    company = data.get('company', 'No company')
    public_repos_count = data.get('public_repos') or 0 
    public_repos = data.get('public_repos') or 0 
    public_gists = data.get('public_gists') or 0 
    followers = data.get('followers') or 0 
    github_id = data.get('id') or 'Unknown'
    node_id = data.get('node_id') or 'Unknown'
    twitter = data.get('twitter_username') or 'No Twitter'
    following = data.get('following') or 0 
    verified = data.get('type', 'User') == 'User'
    profile_url = data.get('html_url') or 'Unknown'

    created_at = datetime.datetime.strptime(
        data['created_at'], "%Y-%m-%dT%H:%M:%SZ"
    ).strftime('%Y-%m-%d %H:%M:%S')

    repos = get_repositories(username)
    if repos:
        repo_list = [repo['name'] for repo in repos]
        most_starred_repo = max(repos, key=lambda r: r['stargazers_count'], default=None)
        most_starred_repo_name = most_starred_repo['name'] if most_starred_repo else "No repos"
        most_starred_repo_stars = most_starred_repo['stargazers_count'] if most_starred_repo else 0
        last_updated_repo = max(repos, key=lambda r: r['updated_at'], default=None)
        last_updated_repo_name = last_updated_repo['name'] if last_updated_repo else "No repos"
        languages = [repo['language'] for repo in repos if repo['language']]
        most_used_language = Counter(languages).most_common(1)
        most_used_language = most_used_language[0][0] if most_used_language else "Unknown"
    else:
        repo_list = []
        most_starred_repo_name = "No repos"
        most_starred_repo_stars = 0
        last_updated_repo_name = "No repos"
        most_used_language = "Unknown"
    pinned_repos = get_pinned_repos(username)
    pinned_repos_str = ", ".join(pinned_repos) if pinned_repos else "No pinned repos"

    results = f"""
        {Fore.WHITE}[ {Fore.BLUE}GitHub Parser Information{Fore.WHITE} ]

    {Fore.BLUE}> + {Fore.WHITE}Username    : {Fore.LIGHTBLACK_EX}{user}
    {Fore.BLUE}> + {Fore.WHITE}GitHub ID   : {Fore.LIGHTBLACK_EX}{github_id}
    {Fore.BLUE}> + {Fore.WHITE}Node ID     : {Fore.LIGHTBLACK_EX}{node_id}
    {Fore.BLUE}> + {Fore.WHITE}Name        : {Fore.LIGHTBLACK_EX}{name}
    {Fore.BLUE}> + {Fore.WHITE}Bio         : {Fore.LIGHTBLACK_EX}{bio}
    {Fore.BLUE}> + {Fore.WHITE}Location    : {Fore.LIGHTBLACK_EX}{location}
    {Fore.BLUE}> + {Fore.WHITE}Created On  : {Fore.LIGHTBLACK_EX}{created_at}
    {Fore.BLUE}> + {Fore.WHITE}Profile URL : {Fore.LIGHTBLACK_EX}{profile_url}

         {Fore.WHITE}[ {Fore.BLUE}Contact Information{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Email   : {Fore.LIGHTBLACK_EX}{email}
    {Fore.BLUE}> + {Fore.WHITE}Blog    : {Fore.LIGHTBLACK_EX}{blog}
    {Fore.BLUE}> + {Fore.WHITE}Company : {Fore.LIGHTBLACK_EX}{company}
    {Fore.BLUE}> + {Fore.WHITE}Twitter : {Fore.LIGHTBLACK_EX}{twitter}

            {Fore.WHITE}[ {Fore.BLUE}Statistics{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Public Repos : {Fore.LIGHTBLACK_EX}{public_repos_count}
    {Fore.BLUE}> + {Fore.WHITE}Public Gists : {Fore.LIGHTBLACK_EX}{public_gists}
    {Fore.BLUE}> + {Fore.WHITE}Followers    : {Fore.LIGHTBLACK_EX}{followers}
    {Fore.BLUE}> + {Fore.WHITE}Following    : {Fore.LIGHTBLACK_EX}{following}

            {Fore.WHITE}[ {Fore.BLUE}Repository Information{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Most Starred Repo   : {Fore.LIGHTBLACK_EX}{most_starred_repo_name} ({most_starred_repo_stars}★)
    {Fore.BLUE}> + {Fore.WHITE}Pinned Repositories : {Fore.LIGHTBLACK_EX}{pinned_repos_str}
    {Fore.BLUE}> + {Fore.WHITE}Most Used Lang      : {Fore.LIGHTBLACK_EX}{most_used_language}
"""
    print(results)
    
    save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
    if save == "y":
        save_path = os.path.join(BASE_DIR, "github_parser.txt")
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(f"""GitHub Parser Information

Username    : {user}
GitHub ID   : {github_id}
Node ID     : {node_id}
Name        : {name}
Bio         : {bio}
Location    : {location}
Created On  : {created_at}
Profile URL : {profile_url}

Contact Information

Email   : {email}
Blog    : {blog}
Company : {company}
Twitter : {twitter}

Statistics

Public Repos : {public_repos_count}
Public Gists : {public_gists}
Followers    : {followers}
Following    : {following}

Repository Information

Most Starred Repo   : {most_starred_repo_name} ({most_starred_repo_stars}★)
Last Updated Repo   : {last_updated_repo_name}
Most Used Language  : {most_used_language}
Pinned Repositories : {pinned_repos_str}
""")
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
        
    elif save == "n":
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
    else:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

    
    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

def github_parser_main():
    while True:
        clear()
        username = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}GitHub{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Username: {Style.RESET_ALL}""")
        if not username:
            print(f"\n{Fore.RED}> ! {Fore.WHITE}Please, enter username\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        github_parser(username)
        break