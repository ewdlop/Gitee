import requests

# Define the necessary variables
access_token = 'your_access_token'  # Replace with your actual access token
owner = 'your_owner'  # Replace with your Gitee username or organization name
repo = 'your_repo'  # Replace with your repository name
branch = 'your_branch'  # Replace with the branch you want to reset

# Gitee API URL to reset a branch
url = f'https://gitee.com/api/v5/repos/{owner}/{repo}/branches/{branch}'

# Headers and payload for the request
headers = {
    'Authorization': f'token {access_token}',
    'Content-Type': 'application/json'
}

# Payload with the SHA of the commit to reset to
payload = {
    'sha': 'new_commit_sha'  # Replace with the SHA of the commit you want to reset the branch to
}

# Make the API request to reset the branch
response = requests.patch(url, headers=headers, json=payload)

# Check the response status
if response.status_code == 200:
    print('Branch reset successfully.')
else:
    print('Failed to reset branch.')
    print('Response:', response.json())
