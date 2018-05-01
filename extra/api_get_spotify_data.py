# -*- coding: utf-8 -*-
"""
Topper:
    
    Gather data on your top 1000 songs on Spotify using API

@author: jsokoll
"""

import spotipy
from spotipy import util

from split import chop

import pandas as pd


uri = "http://localhost/"
CLIENT_ID = "7de0b53d06d94a6a9e2249a297ed0271"
CLIENT_SECRET = "5e711df8d21946ac90fae181b4bff3c0"
scope = 'user-top-read'


def top_n_tracks(n, session):
    """
    n:: Number of Tracks to return
    session:: spotipy session with scope = "user-top-read"

    returns DataFrame
    """

    response = session.current_user_top_tracks(limit=n, time_range="long_term")

    cnt = 1

    fields = ['rank_position', 'album_type', 'album_name', 'album_id',
              'artist_name', 'artist_id', 'track_duration', 'track_id', 
              'track_name', 'track_popularity', 'track_number', 'track_type']
    
    tracks = {}

    for i in fields:
        tracks[i] = []
    
    for i in response['items']:
        tracks['rank_position'].append(cnt)
        tracks['album_type'].append(i['album']['album_type'])
        tracks['album_id'].append(i['album']['id'])
        tracks['album_name'].append(i['album']['name'])
        tracks['artist_name'].append(i['artists'][0]['name'])
        tracks['artist_id'].append(i['artists'][0]['id'])
        tracks['track_duration'].append(i['duration_ms'])
        tracks['track_id'].append(i['id'])
        tracks['track_name'].append(i['name'])
        tracks['track_popularity'].append(i['popularity'])
        tracks['track_number'].append(i['track_number'])
        tracks['track_type'].append(i['type'])
        cnt += 1

    return pd.DataFrame.from_dict(tracks)


def song_features(songs, session):
    """
    Pass list of song ids
    spotipy sessionobject
    
    returns DataFrame
    
    """
    
    chunks = chop(10, songs)
    
    features = []
    
    for c in chunks:
        r = session.audio_features(c)
        
        features.append(r)
        
    features =  [y for x in features for y in x]
        
    df = pd.DataFrame.from_records(features, index=songs)
        
    return df
    

if '__name__' == '__main__':
    
    #Create Session
    token = util.prompt_for_user_token(username = "sokoll.jc",
                                   scope = scope,
                                   client_id= CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   redirect_uri= uri)

    spotify = spotipy.Spotify(auth=token)
    
    
    #Gather the Data
    tracks =  top_n_tracks(1000, spotify)

    features = song_features(tracks['track_id'].tolist(), spotify)
    
    tracks = tracks.merge(features, left_on='track_id', right_index=True)
    
    remove = ['id', 'uri', 'analysis_url', 'track_href']
    
    output = tracks.drop(remove, axis=1)
    output = output.drop_duplicates(subset=['track_id'])

    output.to_csv("C:/Users/jsokoll/Desktop/python_101/extra/UserTopTracks.csv",
                  index=False)