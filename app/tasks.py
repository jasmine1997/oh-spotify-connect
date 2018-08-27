import ohapi
from pprint import pprint
import json
import tempfile
import requests
from celery import shared_task


SPOTIFY_BASE_URL = 'https://api.spotify.com/v1'


@shared_task
def update_play_history(user):

    old_data = get_oh_json(user.oh_member)
    last_time = old_data if old_data else None
    new_data = get_spotify_json(user.spotify_user, last_time)
    final_data = join_json(old_data, new_data)
    put_oh_json(final_data)


def get_oh_json(user):
    data = ohapi.api.exchange_oauth2_member(
        access_token=user.get_access_token()
    )['data']
    pprint(data)
    return data


def get_spotify_json(user, time):
    params = {}
    if time is not None:
        params = {
            'after': time
        }
    recently_played = requests.get(SPOTIFY_BASE_URL + '/me/player/recently-played', headers={
        'Authorization': 'Bearer {}'.format(user.get_access_token())
    }, params=params).json()
    pprint(recently_played)
    return recently_played


def join_json(file, music):
    return None


def put_oh_json(upload):
    # if len(files) > 0:
    #     final_json = requests.get(files[0]['download_url']).json()
    # with open(tempfile.TemporaryFile()) as f:
    #     json.dump(recently_played, f)
    #     ohapi.api.upload_stream(f, "play_history.json", metadata={
    #         "description": "Spotify Play History",
    #         "tags": ["spotify"]
    #     }, access_token=spotify_user.get_access_token())
    return None
