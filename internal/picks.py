import sqlite3

class Pick:
    def __init__(self):
        self.first_name = str
        self.last_name = str
        self.position = str
        self.team = str

    def create_pick(self,
                 first_name,
                 last_name,
                 position,
                 team):
        """Populate draft pick"""
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team



    def add_pick(self, league_name, manager_name):
        """Add  pick into sqlite database"""
        conn = sqlite3.connect('{}.db'.format(league_name))
        cur = conn.cursor()

        cur.execute('''
INSERT INTO {}(manager, player_first_name, player_last_name, position, nfl_team) VALUES(?,?,?,?,?)
    '''.format(league_name),
                    (manager_name, self.first_name, self.last_name, self.position, self.team))
        conn.commit()
        conn.close()
