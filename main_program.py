import requests

def fetch_user_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching repositories: {e}')
        return None
        
    
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f'Error: Status Code {response.status_code}')
        return None
    
      
def display_repository_info(repositories):
    if repositories:
        print("\nUser's Repositories:")
        for repo in repositories:
            print('\nRepository name:', repo['name'])
            print('Description:', repo['description'])
            print('Language:', repo['language'])
            print('Stars:' , repo['stargazers_count'])
        

def main():
    user_input = input("Enter GitHub username: ")
    repositories = fetch_user_repositories(user_input)
    if repositories:
        display_repository_info(repositories)

if __name__ == '__main__':
    main()
