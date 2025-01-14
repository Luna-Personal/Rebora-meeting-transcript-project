from zoom.zoom_api import get_zoom_meetings
from teams.teams_api import get_teams

def main():
    # Fetch Zoom meetings
    zoom_meetings = get_zoom_meetings('your_zoom_user_id')
    print("Zoom Meetings:", zoom_meetings)

    # Fetch Microsoft Teams
    teams = get_teams()
    print("Microsoft Teams:", teams)

if __name__ == "__main__":
    main()