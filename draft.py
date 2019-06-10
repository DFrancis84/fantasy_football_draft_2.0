import sqlite3
import time
import pyfiglet
from prettytable import PrettyTable

def print_banner():
    """Print Title Banner"""
    ascii_banner = pyfiglet.figlet_format('DRAFT.PY')
    print(ascii_banner)

def create_board(league_name):
    """Create DraftBoard"""
    print("Creating DraftBoard for", league_name)
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    # Create table - DraftBoard
    cur.execute('''
    CREATE TABLE IF NOT EXISTS {}(
    pick INTEGER PRIMARY KEY AUTOINCREMENT,
    team TEXT,
    player TEXT,
    position TEXT)
    '''.format(league_name))
    conn.commit()
    conn.close()

def create_team_list(number_teams):
    """Create List of all Teams Drafting"""
    teams = []
    i = 1
    for _ in range(int(number_teams)):
        team = input('Enter name for Team #{}: '.format(i))
        teams.append(team)
        i += 1
    return teams

def select_team(teams):
    """Select Team"""
    i = 1
    for _team_ in teams:
        print("{}. {}".format(i, _team_))
        i += 1
    name = input("Select Team: ")
    name = int(name) - 1
    return teams[name]

def insert_draft_pick(league_name, teams):
    """Insert Draft Picks"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    # Allow input for draft picks
    team_name = select_team(teams)
    player_name = input('Please enter Player Name: ')
    player_position = input('Please enter Players Position: ')
    # Enter draft picks to db
    cur.execute('''
    INSERT INTO {}(team, player, position) VALUES(?,?,?)
    '''.format(league_name), (team_name, player_name, player_position))
    conn.commit()
    conn.close()

def create_table_per_round(league_name, number_teams):
    """Generate Table"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(league_name))
    rows = cur.fetchall()
    table = PrettyTable(['PickNumber', 'TeamName', 'PlayerName', 'PlayerPosition'])
    table.align["TeamName"] = "l"
    table.align["PlayerName"] = "l"
    table.align["PlayerPosition"] = "l"
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3]])
    print("Round {} Complete!".format(len(rows)/int(number_teams)))
    print(table[-int(number_teams):])

def show_draft_results(league_name):
    """Display Draft Results"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    # Select everything from database for table output
    cur.execute("SELECT * FROM {}".format(league_name))
    rows = cur.fetchall()
    # Create and Print display table
    table = PrettyTable(['PickNumber', 'TeamName', 'PlayerName', 'PlayerPosition'])
    table.align["TeamName"] = "l"
    table.align["PlayerName"] = "l"
    table.align["PlayerPosition"] = "l"
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3]])
    print(table)
    conn.close()

def start_draft():
    """Starts the Draft"""
    print_banner()
    league_name = input('Please enter league name: ')
    number_teams = input('How many teams are drafting? ')
    number_rounds = input('How many rounds in this draft? ')
    number_picks = int(number_teams)*int(number_rounds)
    create_board(league_name)
    print("This draft will contain {} picks.".format(number_picks))
    i = 0
    teams = create_team_list(int(number_teams))
    for _ in range(number_picks):
        insert_draft_pick(league_name, teams)
        i += 1
        if i%int(number_teams) == 0:
            create_table_per_round(league_name, number_teams)
        time.sleep(1)
    time.sleep(3)
    print("Your draft is complete for {}!".format(league_name))
    show_draft_results(league_name)

start_draft()
