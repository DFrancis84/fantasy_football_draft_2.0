import sqlite3

class League:
    def __init__(self, league_name):
        self.league_name = league_name

    def create_board(self):
        '''Create DraftBoard'''

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
