#  Copyright (c) 3EMGC 3-2024.

from os import makedirs
from pprint import pformat

import requests

my_token = {'X-Auth-Token': 'ef6212ecbb924c8089341cb6527daaf0'}


def matches():
    # todays' matches of my subscribed competitions
    matches_uri = 'https://api.football-data.org/v4/matches'
    response = requests.get(matches_uri, headers=my_token)
    makedirs('./matches', exist_ok=True)
    with open('matches/matches.ini', '+w') as matches_file:
        matches_file.write(f'{pformat(response.json())}')
    print('Matches Done!')


def teams():
    # Get a list of all the teams
    teams_uri = 'https://api.football-data.org/v4/teams'
    response = requests.get(teams_uri, headers=my_token)
    makedirs('./teams', exist_ok=True)
    with open('./teams/teams.txt', '+w') as matches_file:
        matches_file.write(f'{pformat(response.json())}')
    print('Teams Done!')


def person(id: int):
    # Get the player registred
    person_uri = f'https://api.football-data.org/v4/persons/{id}'
    response = requests.get(person_uri, headers=my_token)
    makedirs('./teams', exist_ok=True)
    with open(f'./teams/person-{id}.txt', '+w') as matches_file:
        matches_file.write(f'{pformat(response.json())}')
    print(f'Person {id} Done!')


def competitions():
    # Get todays' matches of my subscribed competitions
    matches_uri = 'https://api.football-data.org/v4/competitions'
    response = requests.get(matches_uri, headers=my_token)
    makedirs('./competitions', exist_ok=True)
    with open('competitions/competitions.ini', '+w') as competitions_file:
        competitions_file.write(f'{pformat(response.json())}')
    print('Competitions Done!')


def get_championsleague_matches():
    # Get all matches of the Champions League
    comp_uri = 'https://api.football-data.org/v4/competitions/CL/matches'
    response = requests.get(comp_uri, headers=my_token)
    makedirs('./competitions', exist_ok=True)
    with open('competitions/championsleague_matches.json', '+w') as competitions_file:
        competitions_file.write(f'{pformat(response.json())}')
    print('Champions League Done!')


if __name__ == '__main__':
    for id in range(1, 100):
        if id == 10:
            pass
        person(id)
    # matches()
    # teams()
    # competitions()
    # get_championsleague_matches()
