import sqlite3

class League:
    def __init__(self):
        """Enter league parameters"""
        self.league_name = str
        self.number_teams = int
        self.rounds = int
        self.number_picks = int

    def set_league_settings(self):
        league_name = input('Please enter league name: ')
        number_teams = int(input('How many teams are drafting? '))
        number_rounds = int(input('How many rounds in this draft? '))
        number_picks = number_teams*number_rounds
        print("This draft will contain {} picks.".format(number_picks))
        self.league_name = league_name
        self.number_teams = number_teams
        self.rounds = number_rounds
        self.number_picks = number_picks


    def create_board(self):
        """Create DraftBoard"""
        print("Creating DraftBoard for", self.league_name)
        conn = sqlite3.connect('{}.db'.format(self.league_name))
        cur = conn.cursor()
        # Create table - DraftBoard
        cur.execute('''
CREATE TABLE IF NOT EXISTS {}(
pick INTEGER PRIMARY KEY AUTOINCREMENT,
manager TEXT,
player_first_name TEXT,
player_last_name TEXT,
position TEXT,
nfl_team TEXT)
        '''.format(self.league_name))
        conn.commit()
        conn.close()
