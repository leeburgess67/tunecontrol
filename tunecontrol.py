import spotipy
import spotipy.util as util
import keyboard

# Spotify credentials
CLIENT_ID = 'f3399e3e175f451589dfd389d237b4bd'
CLIENT_SECRET = 'c8446fce594a4d14bee1eb22f15fe690'
REDIRECT_URI = 'http://localhost:8888/callback'
USERNAME = 'burgessmetallica'
SCOPE = 'user-modify-playback-state'

# Get token
token = util.prompt_for_user_token(USERNAME, SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)

    # Function to handle play/pause
    def play_pause():
        sp.start_playback() if sp.current_playback()['is_playing'] == False else sp.pause_playback()

    # Function to skip forward
    def skip_forward():
        sp.next_track()

    # Function to skip backward
    def skip_backward():
        sp.previous_track()

    # Register keyboard shortcuts
    keyboard.add_hotkey('ctrl+alt+p', play_pause)
    keyboard.add_hotkey('ctrl+alt+right', skip_forward)
    keyboard.add_hotkey('ctrl+alt+left', skip_backward)

    # Keep the script running
    keyboard.wait('esc')
else:
    print("Can't get token for", USERNAME)
