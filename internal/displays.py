import pyfiglet
import sqlite3
from prettytable import PrettyTable

def print_banner():
    """Print Title Banner"""
    ascii_banner = pyfiglet.figlet_format('DRAFT.PY')
    print(ascii_banner)

def create_table_per_round(league_name, number_teams):
    """Generate Table"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(league_name))
    rows = cur.fetchall()
    table = PrettyTable(['PickNumber',
                         'ManagerName',
                         'PlayerFirstName',
                         'PlayerLastName',
                         'PlayerPosition',
                         'NFLTeam'])
    table.align["ManagerName"] = "l"
    table.align["PlayerFirstName"] = "l"
    table.align["PlayerLastName"] = "l"
    table.align["PlayerPosition"] = "l"
    table.align["NFLTeam"] = "l"
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])
    # Notify that round has been completed
    print("Round {} Complete!".format(len(rows)/int(number_teams)))
    # Prints table at end of each round
    print(table[-int(number_teams):])

def show_draft_picks_by_manager(league_name, manager):
    """Display picks by Manager Name"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()

    cur.execute("""SELECT * FROM {} where manager = '{}'""".format(league_name, manager))
    rows = cur.fetchall()
    table = PrettyTable(['PickNumber',
                         'PlayerFirstName',
                         'PlayerLastName',
                         'PlayerPosition',
                         'NFLTeam'])
    table.align["PlayerFirstName"] = "l"
    table.align["PlayerLastName"] = "l"
    table.align["PlayerPosition"] = "l"
    table.align["NFLTeam"] = "l"
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[2], row[3], row[4], row[5]])
    print(table)

def show_draft_results(league_name):
    """Display Draft Results"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    # Select everything from database for table output
    cur.execute("SELECT * FROM {}".format(league_name))
    rows = cur.fetchall()
    # Create and Print display table
    table = PrettyTable(['PickNumber',
                         'ManagerName',
                         'PlayerFirstName',
                         'PlayerLastName',
                         'PlayerPosition',
                         'NFLTeam'])
    table.align["ManagerName"] = "l"
    table.align["PlayerFirstName"] = "l"
    table.align["PlayerLastName"] = "l"
    table.align["PlayerPosition"] = "l"
    table.align["NFLTeam"] = "l"
    # Iterate through all the rows and add them to prettytable
    for row in rows:
        table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])
    # Prints final draft results
    print(table)
