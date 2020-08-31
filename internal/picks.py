import sqlite3

class Pick:
    def __init__(self,
                 league_name,
                 manager_name,
                 first_name,
                 last_name,
                 position,
                 team):
        self.league_name = league_name
        self.manager_name = manager_name
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team

    def add_pick(self):
        '''Add managers pick into sqlite database'''
        conn = sqlite3.connect('{}.db'.format(self.league_name))
        cur = conn.cursor()

        cur.execute('''
INSERT INTO {}(manager, player_first_name, player_last_name, position, nfl_team) VALUES(?,?,?,?,?)
    '''.format(self.league_name),
                    (self.manager_name, self.first_name, self.last_name, self.position, self.team))
        conn.commit()
        conn.close()


def display_all_picks(league_name):
    '''Displays all picks for certain manager'''
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()

    cur.execute('''SELECT * FROM {}'''.format(league_name))

    rows = cur.fetchall()
    print(rows)
