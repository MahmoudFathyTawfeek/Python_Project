import os      # Importing OS library to read environment variables (like GITHUB_TOKEN)
import sys     # Importing SYS library to exit the script safely in case of errors
import requests # Importing the main library to handle HTTP requests

def github_explorer():
    """
    This script fetches all repositories for a user, sorts them by stars,
    and displays details like language and update date.
    """

    # --- 1. AUTHENTICATION & SECURITY ---
    # We retrieve the token from the system environment for security.
    # NEVER hardcode your token directly in the script.
    token = os.environ.get('GITHUB_TOKEN')

    # Task Requirement: If the token is missing, print an error and exit with code 1.
    if not token:
        print("Error: GITHUB_TOKEN environment variable is missing!")
        sys.exit(1)

    # Prepare headers for the request. 
    # 'Bearer' tells GitHub this is a Personal Access Token.
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json'
    }

    # --- 2. VERIFY USER IDENTITY & ERROR HANDLING ---
    user_url = 'https://api.github.com/user'
    response = requests.get(user_url, headers=headers)
    
    # Task Requirement: Handle non-2xx errors.
    # If the response code is not 200 (OK), print the status and the JSON error message.
    if response.status_code != 200:
        # We use .get('message') so the script doesn't crash if the key is missing.
        error_msg = response.json().get('message', 'Unknown Error')
        print(f"Authentication Error: {response.status_code}")
        print(f"GitHub Message: {error_msg}")
        sys.exit(1) # Exit without showing a messy stack trace

    print(f"Logged in as: {response.json().get('login')}")

    # --- 3. FETCH REPOSITORIES WITH PAGINATION ---
    repos_url = 'https://api.github.com/user/repos'
    # 'per_page' sets how many items per request, 'page' is the starting index.
    params = {'per_page': 100, 'page': 1}
    all_repos = []

    # Loop to "walk" through all pages until no more repositories are found.
    while True:
        print(f"Fetching page {params['page']}...")
        response = requests.get(repos_url, headers=headers, params=params)
        
        # Check for errors during repo fetching.
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            sys.exit(1)

        page_data = response.json()
        
        # If page_data is empty [], it means we have reached the end of the list.
        if not page_data:
            break

        # Add repositories from this page to our main list.
        all_repos.extend(page_data)
        
        # Increment page number for the next iteration of the loop.
        params['page'] += 1

    # --- 4. SORTING BY STARS (Task Requirement #5) ---
    # We sort the list of dictionaries by the 'stargazers_count' key.
    # 'reverse=True' ensures the highest stars appear at the top (Descending).
    all_repos.sort(key=lambda x: x['stargazers_count'], reverse=True)

    # --- 5. PRINTING FORMATTED RESULTS (Task Requirement #4) ---
    print("-" * 60)
    # Formatting headers for a clean table look
    print(f"{'Repository Name':<30} | {'Lang':<10} | {'Stars':<5}")
    print("-" * 60)

    for repo in all_repos:
        # Extracting required fields from the JSON object.
        name = repo['name']
        # If 'language' is null, show "N/A" instead of None.
        lang = repo['language'] if repo['language'] else "N/A"
        stars = repo['stargazers_count']
        
        # Display the data. <30 and <10 ensure columns are aligned.
        print(f"{name:<30} | {lang:<10} | {stars:<5}")
        # Optional: showing the update date as required.
        print(f"   Last Updated: {repo['updated_at']}")
        print("-" * 30)

# Entry point of the script.
if __name__ == "__main__":
    github_explorer()