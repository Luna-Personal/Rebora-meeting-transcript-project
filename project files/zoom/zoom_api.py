import requests
from config import ZOOM_API_KEY, ZOOM_API_SECRET

BASE_URL = 'https://api.zoom.us/v2/'

def get_zoom_meetings(user_id):
    headers = {
        'Authorization': f'Bearer {ZOOM_API_KEY}:{ZOOM_API_SECRET}'
    }
    response = requests.get(f'{BASE_URL}users/{user_id}/meetings', headers=headers)
    return response.json()