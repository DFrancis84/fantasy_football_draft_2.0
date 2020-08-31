"""Fantasy Football Draft Tool"""
import csv
import sqlite3
import time
import pyfiglet
from prettytable import PrettyTable
from internal import board, configs, generate, displays, managers, style


def start_draft():
    """Starts the Draft"""
    # Print program banner
    displays.print_banner()
    # Set League Definitions
    league_name, number_teams, number_rounds, draft_type, number_picks = configs.enter_league_definitions()
    # Create Draft Database
    board.create_board(league_name)
    # Run draft based on designated draft type
    if draft_type == "SNAKE":
        # Create list of teams
        managers_list = managers.create_managers_list_for_snake_draft(int(number_teams), int(number_rounds))
        # Enter draft picks into database
        style.snake_draft(number_picks, number_teams, league_name, managers)
    else:
        # Create list of teams
        managers_list = managers.create_manager_list(int(number_teams))
        # Enter draft picks into database
        style.custom_draft(number_picks, number_teams, league_name, managers_list)
    # Print notification to let user know draft is complete
    print("Your draft is complete for {}!".format(league_name))
    # Small sleep timer for fluiditiy
    time.sleep(3)
    # Display entire draft results
    displays.show_draft_results(league_name)
    # Create csv file from draftboard
    generate.create_csv_from_draft_database(league_name)

start_draft()
