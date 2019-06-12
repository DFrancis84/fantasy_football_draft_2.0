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

def create_manager_list(number_teams):
    """Create List of all Managers Drafting"""
    managers = []
    i = 1
    # Adds a team to the list based on number_teams input
    for _ in range(int(number_teams)):
        manager = input('Enter name for Team #{}: '.format(i))
        managers.append(manager)
        i += 1
    return managers

def create_board(league_name):
    """Create DraftBoard"""
    print("Creating DraftBoard for", league_name)
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    # Create table - DraftBoard
    cur.execute('''
    CREATE TABLE IF NOT EXISTS {}(
    pick INTEGER PRIMARY KEY AUTOINCREMENT,
    manager TEXT,
    player TEXT,
    position TEXT,
    nfl_team TEXT)
    '''.format(league_name))
    conn.commit()
    conn.close()

def insert_draft_pick(league_name, managers):
    """Insert Draft Picks"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    # Allow input for draft picks
    manager_name = select_manager(managers)
    player_name = input('Please enter Players Name: ').capitalize()
    player_position = select_position()
    # player_position = input('Please enter Players Position: ').upper()
    nfl_team = input('Please enter Players Team: ').upper()
    # Enter draft picks to db
    cur.execute('''
    INSERT INTO {}(manager, player, position, nfl_team) VALUES(?,?,?,?)
    '''.format(league_name), (manager_name, player_name, player_position, nfl_team))
    conn.commit()
    conn.close()

def select_manager(managers):
    """Select Manager"""
    _m_ = 1
    # Iterate through list of teams and assign a number
    for _manager_ in managers:
        print("{}. {}".format(_m_, _manager_))
        _m_ += 1
    name = input("Select Manager: ")
    # Takes the users input, and subtracts one since lists start at 0. Converts input into name
    name = int(name) - 1
    return managers[name]

def select_position():
    """Select Position"""
    positions = ["QB", "RB", "WR", "TE", "DST"]
    _p_ = 1
    # Iterate through list of positions and assign a number
    for _position_ in positions:
        print("{}. {}".format(_p_, _position_))
        _p_ += 1
    position = input("Select Position: ")
    # Takes the users input, and subtracts one since lists start at 0. Converts input into name
    position = int(position) - 1
    return positions[position]


def create_table_per_round(league_name, number_teams):
    """Generate Table"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(league_name))
    rows = cur.fetchall()
    table = PrettyTable(['PickNumber', 'ManagerName', 'PlayerName', 'PlayerPosition', 'NFLTeam'])
    table.align["ManagerName"] = "l"
    table.align["PlayerName"] = "l"
    table.align["PlayerPosition"] = "l"
    table.align["NFLTeam"] = "l"
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3], row[4]])
    # Notify that round has been completed
    print("Round {} Complete!".format(len(rows)/int(number_teams)))
    # Prints table at end of each round
    print(table[-int(number_teams):])

def draft(number_picks, number_teams, league_name, managers):
    """The Entire Draft Process"""
    _r_ = 0
    for _ in range(number_picks):
        insert_draft_pick(league_name, managers)
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
    table = PrettyTable(['PickNumber', 'ManagerName', 'PlayerName', 'PlayerPosition', 'NFLTeam'])
    table.align["ManagerName"] = "l"
    table.align["PlayerName"] = "l"
    table.align["PlayerPosition"] = "l"
    table.align["NFLTeam"] = "l"
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3], row[4]])
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
    managers = create_manager_list(int(number_teams))
    # Enter draft picks into database
    draft(number_picks, number_teams, league_name, managers)
    # Print notification to let user know draft is complete
    print("Your draft is complete for {}!".format(league_name))
    # Small sleep timer for fluiditiy
    time.sleep(3)
    # Display entire draft results
    show_draft_results(league_name)

start_draft()
