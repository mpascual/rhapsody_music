#!/usr/bin/env python
#
# Fetch playlist from rhapsody.com music service and all songs, write to a file
#

import json
import requests
import yaml

CONFIG = None
api_url = 'https://api.rhapsody.com/v1'

def init():
    global CONFIG
    global headers
    with open('creds.yml', 'r') as stream:
        CONFIG = yaml.load(stream.read())
    headers = {'Authorization': 'Bearer {0}'.format(CONFIG
                                                    ['creds']['access_token'])}

def playlist():
    playlist_url = '{0}/me/playlists'.format(api_url)
    playlist = requests.get(playlist_url, headers=headers)
    results = json.loads(playlist.text)
    count = 0
    for r in results:
        print 'Playlist: {0}'.format(r['name'])
        print '-'
        playlist_tracks(playlist_id=r['id'], playlist_name=r['name'])
        #count += 1
    #print 'Total: {0}'.format(count)

def playlist_tracks(playlist_id, playlist_name):
    tracks_url = '{0}/me/playlists/{1}'.format(api_url, playlist_id)
    tracks = requests.get(tracks_url, headers=headers)
    results = json.loads(tracks.text)
    for r in results['tracks']:
        artist = r['artist']['name']
        song = r['name']
        print '{0} - {1}'.format(artist.encode('utf-8'), song.encode('utf-8'))
    print

if __name__ == '__main__':
    init()
    playlist()


