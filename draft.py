"""Fantasy Football Draft Tool"""
import sqlite3
import time
import pyfiglet
from prettytable import PrettyTable

def print_banner():
    """Print Title Banner"""
    ascii_banner = pyfiglet.figlet_format('DRAFT.PY')
    print(ascii_banner)

def enter_league_definitions():
    """Enter league parameters"""
    league_name = input('Please enter league name: ')
    number_teams = input('How many teams are drafting? ')
    number_rounds = input('How many rounds in this draft? ')
    number_picks = int(number_teams)*int(number_rounds)
    print("This draft will contain {} picks.".format(number_picks))
    return league_name, number_teams, number_picks

def create_team_list(number_teams):
    """Create List of all Teams Drafting"""
    teams = []
    i = 1
    # Adds a team to the list based on number_teams input
    for _ in range(int(number_teams)):
        team = input('Enter name for Team #{}: '.format(i))
        teams.append(team)
        i += 1
    return teams

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

def select_team(teams):
    """Select Team"""
    _t_ = 1
    # Iterate through list of teams and assign a number
    for _team_ in teams:
        print("{}. {}".format(_t_, _team_))
        _t_ += 1
    name = input("Select Team: ")
    # Takes the users input, and subtracts one since lists start at 0. Converts input into name
    name = int(name) - 1
    return teams[name]

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
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3]])
    # Notify that round has been completed
    print("Round {} Complete!".format(len(rows)/int(number_teams)))
    # Prints table at end of each round
    print(table[-int(number_teams):])

def draft(number_picks, number_teams, league_name, teams):
    """The Entire Draft Process"""
    _r_ = 0
    for _ in range(number_picks):
        insert_draft_pick(league_name, teams)
        _r_ += 1
        if _r_%int(number_teams) == 0:
            create_table_per_round(league_name, number_teams)
        time.sleep(1)

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
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3]])
    # Prints final draft results
    print(table)

def start_draft():
    """Starts the Draft"""
    # Print program banner
    print_banner()
    # Set League Definitions
    league_name, number_teams, number_picks = enter_league_definitions()
    # Create Draft Database
    create_board(league_name)
    # Create list of teams
    teams = create_team_list(int(number_teams))
    # Enter draft picks into database
    draft(number_picks, number_teams, league_name, teams)
    # Print notification to let user know draft is complete
    print("Your draft is complete for {}!".format(league_name))
    # Small sleep timer for fluiditiy
    time.sleep(3)
    # Display entire draft results
    show_draft_results(league_name)

start_draft()
