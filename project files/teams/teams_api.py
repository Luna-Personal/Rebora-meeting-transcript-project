import requests
from config import TEAMS_CLIENT_ID, TEAMS_CLIENT_SECRET, TEAMS_TENANT_ID

AUTH_URL = f'https://login.microsoftonline.com/{TEAMS_TENANT_ID}/oauth2/v2.0/token'
GRAPH_URL = 'https://graph.microsoft.com/v1.0/'

def get_access_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': TEAMS_CLIENT_ID,
        'client_secret': TEAMS_CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(AUTH_URL, data=data)
    return response.json().get('access_token')


def get_teams():
    token = get_access_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f'{GRAPH_URL}me/joinedTeams', headers=headers)
    return response.json()